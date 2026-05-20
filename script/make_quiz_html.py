import argparse
import hashlib
import json
import re
from pathlib import Path


QUESTION_NUMBER_RE = re.compile(r"^(?:#+\s*)?\d+\.$")
ANSWER_RE = re.compile(r"^[A-D]$")
NUMBERED_ANSWER_RE = re.compile(r"^\d+\.\s*([A-D])$")
OPTION_RE = re.compile(r"^([A-D])\.\s*(.+)$")


def split_source(text):
    lines = [line.rstrip() for line in text.splitlines()]

    answer_start = None
    for index, line in enumerate(lines):
        stripped = line.strip()
        if stripped.lower() in {"# answer key", "## answer key", "answer key"}:
            answer_start = index + 1
            break

        if ANSWER_RE.match(stripped):
            remaining = [item.strip() for item in lines[index:] if item.strip()]
            if remaining and all(ANSWER_RE.match(item) for item in remaining):
                answer_start = index
                break

    if answer_start is None:
        raise ValueError("Could not find the answer key block at the end of the file.")

    question_lines = lines[:answer_start]
    answers = parse_answers(lines[answer_start:])
    questions = parse_questions(question_lines)

    if len(questions) != len(answers):
        raise ValueError(f"Found {len(questions)} questions but {len(answers)} answers.")

    for question, answer in zip(questions, answers):
        question["answer"] = answer

    return questions


def parse_answers(lines):
    answers = []

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped == "---":
            continue

        numbered_match = NUMBERED_ANSWER_RE.match(stripped)
        if numbered_match:
            answers.append(numbered_match.group(1))
            continue

        if ANSWER_RE.match(stripped):
            answers.append(stripped)

    return answers


def parse_questions(lines):
    questions = []
    current = []

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped == "---" or stripped.lower() in {"# answer key", "## answer key", "answer key"}:
            continue
        if QUESTION_NUMBER_RE.match(stripped):
            if current:
                questions.append(parse_question(current))
                current = []
            continue
        current.append(stripped)

    if current:
        questions.append(parse_question(current))

    return questions


def parse_question(lines):
    stem = []
    options = {}

    for line in lines:
        option_match = OPTION_RE.match(line)
        if option_match:
            options[option_match.group(1)] = option_match.group(2)
        else:
            stem.append(line)

    if set(options) != {"A", "B", "C", "D"}:
        raise ValueError(f"Question is missing options: {' '.join(lines)}")

    return {
        "question": " ".join(stem),
        "options": options,
    }


def file_hash(path):
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return f"{int(digest, 16) % 1000000:06d}"


def display_name_from_stem(stem):
    words = re.split(r"[\s_-]+", stem.strip())
    return " ".join(word[:1].upper() + word[1:] for word in words if word)


def build_html(questions, quiz_name, quiz_code):
    questions_json = json.dumps(questions, ensure_ascii=False)
    quiz_name_json = json.dumps(quiz_name, ensure_ascii=False)
    quiz_code_json = json.dumps(quiz_code, ensure_ascii=False)
    return f"""<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{quiz_name} - {quiz_code}</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f6f7f9;
      --panel: #ffffff;
      --text: #1f2933;
      --muted: #667085;
      --line: #d6dbe3;
      --accent: #2563eb;
      --accent-soft: #e8f0ff;
      --ok: #15803d;
      --bad: #b42318;
    }}

    * {{
      box-sizing: border-box;
    }}

    body {{
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: Arial, Helvetica, sans-serif;
      line-height: 1.5;
    }}

    header {{
      position: sticky;
      top: 0;
      z-index: 10;
      background: rgba(255, 255, 255, 0.96);
      border-bottom: 1px solid var(--line);
    }}

    .bar {{
      max-width: 980px;
      margin: 0 auto;
      padding: 14px 18px;
      display: flex;
      gap: 12px;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
    }}

    h1 {{
      margin: 0;
      font-size: 20px;
    }}

    .status {{
      color: var(--muted);
      font-size: 14px;
      display: flex;
      gap: 12px;
      align-items: center;
      flex-wrap: wrap;
    }}

    main {{
      max-width: 980px;
      margin: 0 auto;
      padding: 18px;
    }}

    .question {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 18px;
      margin-bottom: 14px;
    }}

    .start-panel {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 22px;
      margin-bottom: 18px;
    }}

    .start-panel h2 {{
      margin: 0 0 8px;
      font-size: 22px;
    }}

    .start-panel p {{
      margin: 0 0 16px;
      color: var(--muted);
    }}

    .hidden {{
      display: none;
    }}

    .question-title {{
      display: flex;
      gap: 10px;
      align-items: flex-start;
      margin-bottom: 14px;
      font-weight: 700;
    }}

    .number {{
      flex: 0 0 auto;
      min-width: 34px;
      color: var(--accent);
    }}

    .options {{
      display: grid;
      gap: 8px;
    }}

    label.option {{
      display: flex;
      gap: 10px;
      align-items: flex-start;
      border: 1px solid var(--line);
      border-radius: 7px;
      padding: 10px 12px;
      cursor: pointer;
      background: #fff;
    }}

    label.option:hover {{
      border-color: var(--accent);
      background: var(--accent-soft);
    }}

    label.option.selected {{
      border-color: var(--accent);
      background: var(--accent-soft);
    }}

    label.option.correct {{
      border-color: var(--ok);
      background: #eaf8ef;
    }}

    label.option.wrong {{
      border-color: var(--bad);
      background: #fff0ee;
    }}

    input[type="radio"] {{
      margin-top: 4px;
    }}

    .actions {{
      position: sticky;
      bottom: 0;
      background: rgba(246, 247, 249, 0.96);
      border-top: 1px solid var(--line);
      padding: 14px 0;
      margin-top: 20px;
    }}

    .actions-inner {{
      display: flex;
      gap: 10px;
      align-items: center;
      flex-wrap: wrap;
    }}

    button {{
      border: 1px solid var(--accent);
      background: var(--accent);
      color: #fff;
      border-radius: 7px;
      padding: 10px 14px;
      font-weight: 700;
      cursor: pointer;
    }}

    button.secondary {{
      background: #fff;
      color: var(--accent);
    }}

    textarea {{
      width: 100%;
      min-height: 110px;
      margin-top: 12px;
      padding: 10px;
      border: 1px solid var(--line);
      border-radius: 7px;
      font-family: Consolas, Monaco, monospace;
      font-size: 13px;
      resize: vertical;
    }}

    .result {{
      margin-top: 12px;
      font-weight: 700;
    }}

    @media (max-width: 640px) {{
      .bar {{
        align-items: flex-start;
      }}

      h1 {{
        font-size: 18px;
      }}

      .question {{
        padding: 14px;
      }}
    }}
  </style>
</head>
<body>
  <header>
    <div class="bar">
      <h1 id="quizTitle">Security Quiz</h1>
      <div class="status">
        <span>Code: <strong id="quizCode"></strong></span>
        <span><span id="answeredCount">0</span>/<span id="totalCount">0</span> answered</span>
        <span>Time: <strong id="timerText">00:00:00</strong></span>
      </div>
    </div>
  </header>

  <main>
    <section class="start-panel" id="startPanel">
      <h2 id="startTitle"></h2>
      <p>Ma de: <strong id="startCode"></strong> · So cau: <strong id="startTotal"></strong></p>
      <button type="button" id="startButton">Bat dau lam bai</button>
    </section>

    <form id="quizForm" class="hidden"></form>

    <section class="actions hidden" id="actionsPanel">
      <div class="actions-inner">
        <button type="button" id="gradeButton">Chấm bài</button>
        <button type="button" class="secondary" id="exportButton">Xuất chuỗi kết quả</button>
        <button type="button" class="secondary" id="copyButton">Copy chuỗi</button>
        <button type="button" class="secondary" id="resetButton">Làm lại</button>
      </div>
      <div class="result" id="scoreText"></div>
      <textarea id="exportText" readonly placeholder="Chuỗi kết quả sẽ hiện ở đây sau khi bấm Xuất chuỗi kết quả."></textarea>
    </section>
  </main>

  <script>
    const quizName = {quiz_name_json};
    const quizCode = {quiz_code_json};
    const questions = {questions_json};
    const selected = new Array(questions.length).fill("");

    const quizForm = document.getElementById("quizForm");
    const quizTitle = document.getElementById("quizTitle");
    const quizCodeElement = document.getElementById("quizCode");
    const startPanel = document.getElementById("startPanel");
    const startTitle = document.getElementById("startTitle");
    const startCode = document.getElementById("startCode");
    const startTotal = document.getElementById("startTotal");
    const actionsPanel = document.getElementById("actionsPanel");
    const answeredCount = document.getElementById("answeredCount");
    const totalCount = document.getElementById("totalCount");
    const timerText = document.getElementById("timerText");
    const scoreText = document.getElementById("scoreText");
    const exportText = document.getElementById("exportText");
    let startedAt = null;
    let elapsedSeconds = 0;
    let timerId = null;

    quizTitle.textContent = quizName;
    quizCodeElement.textContent = quizCode;
    startTitle.textContent = quizName;
    startCode.textContent = quizCode;
    startTotal.textContent = questions.length;
    totalCount.textContent = questions.length;

    function renderQuiz() {{
      quizForm.innerHTML = questions.map((item, index) => {{
        const questionNumber = index + 1;
        const options = ["A", "B", "C", "D"].map(letter => `
          <label class="option" data-question="${{index}}" data-choice="${{letter}}">
            <input type="radio" name="q${{index}}" value="${{letter}}">
            <span><strong>${{letter}}.</strong> ${{escapeHtml(item.options[letter])}}</span>
          </label>
        `).join("");

        return `
          <article class="question" id="question-${{questionNumber}}">
            <div class="question-title">
              <span class="number">${{questionNumber}}.</span>
              <span>${{escapeHtml(item.question)}}</span>
            </div>
            <div class="options">${{options}}</div>
          </article>
        `;
      }}).join("");
    }}

    function escapeHtml(value) {{
      return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
    }}

    function updateAnsweredCount() {{
      answeredCount.textContent = selected.filter(Boolean).length;
    }}

    function formatDuration(totalSeconds) {{
      const hours = Math.floor(totalSeconds / 3600);
      const minutes = Math.floor((totalSeconds % 3600) / 60);
      const seconds = totalSeconds % 60;
      return [hours, minutes, seconds]
        .map(value => String(value).padStart(2, "0"))
        .join(":");
    }}

    function updateTimer() {{
      if (!startedAt) {{
        return;
      }}
      elapsedSeconds = Math.floor((Date.now() - startedAt) / 1000);
      timerText.textContent = formatDuration(elapsedSeconds);
    }}

    function resetTimer() {{
      startedAt = null;
      elapsedSeconds = 0;
      timerText.textContent = "00:00:00";
      if (timerId) {{
        clearInterval(timerId);
        timerId = null;
      }}
    }}

    function startQuiz() {{
      startPanel.classList.add("hidden");
      quizForm.classList.remove("hidden");
      actionsPanel.classList.remove("hidden");
      startedAt = Date.now();
      updateTimer();
      timerId = setInterval(updateTimer, 1000);
    }}

    function clearMarks() {{
      document.querySelectorAll(".option").forEach(option => {{
        option.classList.remove("selected", "correct", "wrong");
      }});
    }}

    function gradeQuiz() {{
      let correct = 0;
      clearMarks();

      questions.forEach((item, index) => {{
        const answer = item.answer;
        const choice = selected[index];
        const correctOption = document.querySelector(`[data-question="${{index}}"][data-choice="${{answer}}"]`);
        correctOption.classList.add("correct");

        if (choice === answer) {{
          correct += 1;
        }} else if (choice) {{
          const wrongOption = document.querySelector(`[data-question="${{index}}"][data-choice="${{choice}}"]`);
          wrongOption.classList.add("wrong");
        }}
      }});

      scoreText.textContent = `Điểm: ${{correct}}/${{questions.length}} (${{Math.round(correct / questions.length * 100)}}%)`;
      return correct;
    }}

    function buildExportString() {{
      const correct = questions.reduce((count, item, index) => (
        count + (selected[index] === item.answer ? 1 : 0)
      ), 0);

      const answers = selected.map((choice, index) => `${{index + 1}}:${{choice || "-"}}`).join(",");
      const wrong = questions
        .map((item, index) => selected[index] === item.answer ? "" : `${{index + 1}}:${{selected[index] || "-"}}>${{item.answer}}`)
        .filter(Boolean)
        .join(",");

      updateTimer();
      return `quiz=${{quizName}};code=${{quizCode}};score=${{correct}}/${{questions.length}};time=${{formatDuration(elapsedSeconds)}};seconds=${{elapsedSeconds}};answers=${{answers}};wrong=${{wrong || "none"}}`;
    }}

    quizForm.addEventListener("change", event => {{
      if (!event.target.matches('input[type="radio"]')) return;

      const index = Number(event.target.name.replace("q", ""));
      selected[index] = event.target.value;

      document.querySelectorAll(`[data-question="${{index}}"]`).forEach(option => {{
        option.classList.toggle("selected", option.dataset.choice === selected[index]);
        option.classList.remove("correct", "wrong");
      }});

      scoreText.textContent = "";
      updateAnsweredCount();
    }});

    document.getElementById("gradeButton").addEventListener("click", gradeQuiz);
    document.getElementById("startButton").addEventListener("click", startQuiz);

    document.getElementById("exportButton").addEventListener("click", () => {{
      gradeQuiz();
      exportText.value = buildExportString();
      exportText.focus();
      exportText.select();
    }});

    document.getElementById("copyButton").addEventListener("click", async () => {{
      if (!exportText.value) {{
        exportText.value = buildExportString();
      }}

      exportText.focus();
      exportText.select();

      try {{
        await navigator.clipboard.writeText(exportText.value);
        scoreText.textContent = "Đã copy chuỗi kết quả.";
      }} catch {{
        document.execCommand("copy");
        scoreText.textContent = "Đã chọn chuỗi kết quả, bạn có thể copy thủ công nếu trình duyệt chặn.";
      }}
    }});

    document.getElementById("resetButton").addEventListener("click", () => {{
      selected.fill("");
      quizForm.reset();
      clearMarks();
      scoreText.textContent = "";
      exportText.value = "";
      updateAnsweredCount();
      resetTimer();
      startPanel.classList.remove("hidden");
      quizForm.classList.add("hidden");
      actionsPanel.classList.add("hidden");
      window.scrollTo({{ top: 0, behavior: "smooth" }});
    }});

    renderQuiz();
    updateAnsweredCount();
    resetTimer();
  </script>
</body>
</html>
"""


def build_one(source_path, output_path):
    questions = split_source(source_path.read_text(encoding="utf-8-sig"))
    quiz_code = file_hash(source_path)
    quiz_name = display_name_from_stem(source_path.stem)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(build_html(questions, quiz_name, quiz_code), encoding="utf-8")
    return {
        "name": quiz_name,
        "code": quiz_code,
        "question_count": len(questions),
        "file": output_path.name,
    }


def build_menu_html(quizzes):
    items = "\n".join(
        f"""        <a class="quiz-link" href="{quiz['file']}">
          <span>
            <strong>{quiz['name']}</strong>
            <small>Quiz code {quiz['code']} · {quiz['question_count']} questions</small>
          </span>
          <span class="arrow">Open</span>
        </a>"""
        for quiz in quizzes
    )
    return f"""<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Quiz Menu</title>
  <style>
    :root {{
      --bg: #f6f7f9;
      --panel: #ffffff;
      --text: #1f2933;
      --muted: #667085;
      --line: #d6dbe3;
      --accent: #2563eb;
      --accent-soft: #e8f0ff;
    }}

    * {{
      box-sizing: border-box;
    }}

    body {{
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: Arial, Helvetica, sans-serif;
      line-height: 1.5;
    }}

    main {{
      max-width: 860px;
      margin: 0 auto;
      padding: 28px 18px;
    }}

    h1 {{
      margin: 0 0 6px;
      font-size: 28px;
    }}

    p {{
      margin: 0 0 22px;
      color: var(--muted);
    }}

    .list {{
      display: grid;
      gap: 10px;
    }}

    .quiz-link {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      padding: 16px;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      color: inherit;
      text-decoration: none;
    }}

    .quiz-link:hover {{
      border-color: var(--accent);
      background: var(--accent-soft);
    }}

    strong {{
      display: block;
      font-size: 18px;
    }}

    small {{
      display: block;
      color: var(--muted);
      margin-top: 2px;
    }}

    .arrow {{
      color: var(--accent);
      font-weight: 700;
      white-space: nowrap;
    }}
  </style>
</head>
<body>
  <main>
    <h1>Choose a Quiz</h1>
    <p>The timer starts only after you open a quiz and press Start.</p>
    <div class="list">
{items}
    </div>
  </main>
</body>
</html>
"""


def write_menu(asset_dir, quizzes):
    menu_path = asset_dir / "index.html"
    menu_path.write_text(build_menu_html(quizzes), encoding="utf-8")
    return menu_path


def main():
    parser = argparse.ArgumentParser(description="Create interactive HTML quizzes from files in data.")
    parser.add_argument("--data-dir", default="data", help="Directory containing question text files.")
    parser.add_argument("--asset-dir", default="asset", help="Directory for generated HTML files.")
    parser.add_argument("--source", help="Optional single input question file.")
    parser.add_argument("--output", help="Optional single output HTML file.")
    args = parser.parse_args()

    if args.source:
        source_path = Path(args.source)
        output_path = Path(args.output) if args.output else Path(args.asset_dir) / f"{source_path.stem}.html"
        quiz = build_one(source_path, output_path)
        print(f"Wrote {quiz['question_count']} questions to {output_path} code={quiz['code']}")
        return

    data_dir = Path(args.data_dir)
    asset_dir = Path(args.asset_dir)
    source_paths = sorted(data_dir.glob("*.txt"))

    if not source_paths:
        raise ValueError(f"No .txt quiz files found in {data_dir}")

    quizzes = []
    for source_path in source_paths:
        output_path = asset_dir / f"{source_path.stem}.html"
        quiz = build_one(source_path, output_path)
        quizzes.append(quiz)
        print(f"Wrote {quiz['question_count']} questions to {output_path} code={quiz['code']}")

    menu_path = write_menu(asset_dir, quizzes)
    print(f"Wrote menu to {menu_path}")


if __name__ == "__main__":
    main()
