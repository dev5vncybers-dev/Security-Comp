# Security+ SY0-701 — Module 5: Security Program Management and Oversight

> Mục tiêu: Đây là bản tổng hợp kiến thức cần học cho **Module 5 — Security Program Management and Oversight / Governance, Risk, and Compliance**.  
> Module này chiếm khoảng **20%** bài thi SY0-701. Đây là phần thiên về policy, risk, compliance, audit, third-party risk và security awareness.

---

## 0. Tổng quan Module 5

Module 5 tập trung vào:

- Security governance
- Policies, standards, procedures, guidelines
- Risk management
- Risk analysis
- Business impact analysis
- Third-party risk management
- Agreement types
- Compliance and privacy
- Audits and assessments
- Security awareness and user training

Nếu Module 4 là “vận hành kỹ thuật”, thì Module 5 là “quản trị, rủi ro, tuân thủ và chương trình bảo mật”.

---

# 5.1 — Security Governance

## 5.1.1 Governance là gì?

Governance là cách tổ chức đặt mục tiêu bảo mật, phân quyền trách nhiệm, tạo chính sách, quản lý rủi ro, đảm bảo compliance và đo lường security program.

```text
Governance = direction + accountability + policy + oversight
```

## 5.1.2 Policy, Standard, Procedure, Guideline

| Term | Nghĩa | Mức bắt buộc | Ví dụ |
|---|---|---|---|
| Policy | Chính sách cấp cao | Bắt buộc | Company must protect PII |
| Standard | Chuẩn cụ thể phải theo | Bắt buộc | Password minimum 14 characters |
| Procedure | Các bước thực hiện | Bắt buộc nếu được ban hành | Step-by-step reset password |
| Guideline | Khuyến nghị | Không bắt buộc tuyệt đối | Recommended secure coding style |

```text
Policy = What/Why
Standard = Specific requirement
Procedure = Step-by-step
Guideline = Recommendation
```

## 5.1.3 Security Policies

| Policy | Purpose |
|---|---|
| Acceptable Use Policy | Quy định cách dùng tài nguyên công ty |
| Information Security Policy | Chính sách bảo mật tổng thể |
| Data Classification Policy | Phân loại dữ liệu |
| Access Control Policy | Quy định cấp quyền |
| Password Policy | Quy định mật khẩu |
| Remote Access Policy | Quy định VPN/remote access |
| Incident Response Policy | Quy định xử lý sự cố |
| Change Management Policy | Quy định thay đổi hệ thống |
| Data Retention Policy | Quy định lưu giữ dữ liệu |
| Clean Desk Policy | Không để tài liệu nhạy cảm trên bàn |
| BYOD Policy | Quy định thiết bị cá nhân |

## 5.1.4 Exceptions and Exemptions

| Term | Meaning |
|---|---|
| Exception | Ngoại lệ tạm thời khỏi policy/standard |
| Exemption | Miễn trừ khỏi yêu cầu trong một trường hợp cụ thể |
| Compensating control | Control thay thế để giảm rủi ro |
| Risk acceptance | Chấp nhận rủi ro còn lại |

Nếu không thể patch hệ thống legacy: tạo exception có phê duyệt, ghi rõ thời hạn, áp dụng compensating control và review định kỳ.

## 5.1.5 Security Considerations

| Consideration | Ví dụ |
|---|---|
| Regulatory | SOX, HIPAA, GDPR, PCI DSS |
| Legal | Breach notification, legal hold |
| Industry | Healthcare, finance, utilities |
| Geographical | Luật thay đổi theo quốc gia/khu vực |

Ví dụ nhanh:

- Healthcare → HIPAA, PHI
- Payment cards → PCI DSS
- Public companies → SOX
- EU personal data → GDPR
- Data location → data sovereignty

## 5.1.6 Data Roles and Responsibilities

| Role | Meaning |
|---|---|
| Data owner | Người chịu trách nhiệm/accountable cho dữ liệu |
| Data controller | Quyết định mục đích và cách xử lý personal data |
| Data processor | Xử lý dữ liệu thay cho controller |
| Data custodian/steward | Quản lý vận hành, bảo vệ, phân loại, access |

```text
Owner = accountable
Controller = decides why/how data is processed
Processor = processes for controller
Custodian/Steward = protects and manages data day-to-day
```

---

# 5.2 — Risk Management

## 5.2.1 Risk là gì?

Risk là khả năng một threat khai thác vulnerability gây impact.

```text
Risk = Threat x Vulnerability x Impact
```

Ví dụ:

- Threat: attacker
- Vulnerability: exposed RDP
- Impact: ransomware, downtime, data loss

## 5.2.2 Risk Management Process

```text
Identify → Analyze → Prioritize → Treat → Monitor
```

| Step | Meaning |
|---|---|
| Identify | Xác định rủi ro |
| Analyze | Phân tích likelihood/impact |
| Prioritize | Ưu tiên xử lý |
| Treat | Chọn strategy |
| Monitor | Theo dõi rủi ro còn lại |

## 5.2.3 Risk Assessment Types

| Type | Meaning | Ví dụ |
|---|---|---|
| Qualitative | Định tính | Low/Medium/High |
| Quantitative | Định lượng | Tính bằng tiền, số liệu |
| Semi-quantitative | Kết hợp điểm số | Scale 1–5, risk matrix |

```text
Qualitative = words/levels
Quantitative = money/numbers
```

## 5.2.4 Quantitative Risk Formulas

| Term | Meaning |
|---|---|
| AV | Asset Value |
| EF | Exposure Factor |
| SLE | Single Loss Expectancy |
| ARO | Annualized Rate of Occurrence |
| ALE | Annualized Loss Expectancy |

```text
SLE = AV x EF
ALE = SLE x ARO
```

Ví dụ:

```text
Asset value = $100,000
Exposure factor = 25%
SLE = $25,000

ARO = 2
ALE = $25,000 x 2 = $50,000/year
```

```text
SLE = mất bao nhiêu mỗi lần
ARO = xảy ra bao nhiêu lần mỗi năm
ALE = mất bao nhiêu mỗi năm
```

## 5.2.5 Risk Management Strategies

| Strategy | Meaning | Ví dụ |
|---|---|---|
| Mitigate | Giảm rủi ro | Patch, firewall, MFA |
| Accept | Chấp nhận rủi ro | Risk thấp, chi phí fix quá cao |
| Transfer | Chuyển giao rủi ro | Cyber insurance, outsource |
| Avoid | Tránh rủi ro | Không triển khai dịch vụ nguy hiểm |
| Exemption | Miễn trừ có phê duyệt | Legacy system chưa thể patch |

| Tình huống | Strategy |
|---|---|
| Mua bảo hiểm | Transfer |
| Vá lỗi | Mitigate |
| Không làm dự án | Avoid |
| Chấp nhận vì chi phí sửa quá cao | Accept |
| Không thể tuân thủ tạm thời có phê duyệt | Exception/Exemption |

## 5.2.6 Risk Register

Risk register là danh sách rủi ro được theo dõi.

Thường có:

- risk description
- owner
- likelihood
- impact
- score
- treatment plan
- residual risk
- status
- review date

## 5.2.7 Risk Appetite, Tolerance, Threshold

| Term | Meaning |
|---|---|
| Risk appetite | Mức rủi ro tổ chức sẵn sàng chấp nhận |
| Risk tolerance | Mức dao động có thể chấp nhận |
| Risk threshold | Ngưỡng mà vượt qua thì phải hành động |

```text
Appetite = muốn ăn bao nhiêu rủi ro
Tolerance = chịu được dao động bao nhiêu
Threshold = vượt ngưỡng thì xử lý
```

## 5.2.8 Residual Risk

Residual risk là rủi ro còn lại sau khi đã áp control.

```text
Inherent risk - controls = residual risk
```

## 5.2.9 Business Impact Analysis — BIA

BIA xác định tác động kinh doanh nếu hệ thống/dịch vụ bị gián đoạn.

| Term | Meaning |
|---|---|
| Critical business functions | Chức năng kinh doanh quan trọng |
| Dependencies | Phụ thuộc giữa hệ thống/quy trình |
| Impact | Tài chính, vận hành, pháp lý, uy tín |
| RTO | Recovery Time Objective |
| RPO | Recovery Point Objective |
| MTTR | Mean Time to Repair/Recover |
| MTBF | Mean Time Between Failures |

## 5.2.10 RTO vs RPO

| Term | Meaning | Câu hỏi cần trả lời |
|---|---|---|
| RTO | Thời gian tối đa để khôi phục | Down được bao lâu? |
| RPO | Mức dữ liệu tối đa có thể mất | Mất dữ liệu được bao lâu? |

```text
RTO = time to recover service
RPO = point of data recovery
```

---

# 5.3 — Third-party Risk Management

## 5.3.1 Third-party Risk là gì?

Third-party risk là rủi ro từ:

- vendor
- supplier
- MSP
- cloud provider
- contractor
- partner
- SaaS provider

## 5.3.2 Vendor Due Diligence

Due diligence là kiểm tra, đánh giá trước khi hợp tác.

Cần xem:

- financial stability
- security posture
- compliance certifications
- background checks
- incident history
- data handling
- disaster recovery
- access control
- subcontractors
- conflict of interest

## 5.3.3 Due Care vs Due Diligence

| Term | Meaning |
|---|---|
| Due care | Hành động có trách nhiệm |
| Due diligence | Điều tra/đánh giá trước khi hành động |

```text
Due diligence = investigate
Due care = act responsibly
```

## 5.3.4 Vendor Monitoring

Vendor monitoring không kết thúc sau khi ký hợp đồng.

Cần:

- regular review
- security questionnaire
- audit reports
- SLA review
- financial health check
- breach/news monitoring
- access review
- performance review

## 5.3.5 Questionnaires

Security questionnaire dùng để hỏi vendor:

- có DR plan không?
- dữ liệu được mã hóa thế nào?
- có security awareness không?
- access control ra sao?
- incident notification trong bao lâu?
- có third-party audit không?
- retention và deletion policy thế nào?

## 5.3.6 Rules of Engagement — ROE

ROE xác định phạm vi và quy tắc kiểm thử.

Nội dung:

- purpose
- scope
- testing type
- schedule
- IP/domain in-scope
- out-of-scope systems
- emergency contacts
- sensitive data handling
- allowed/disallowed techniques

Nếu câu hỏi nói pentest cần xác định scope, schedule, IP ranges, emergency contacts → ROE.

## 5.3.7 Agreement Types

| Agreement | Meaning | Keyword |
|---|---|---|
| SLA | Service Level Agreement | uptime, response time |
| MOU | Memorandum of Understanding | informal understanding, common goals |
| MOA | Memorandum of Agreement | stronger than MOU, conditional agreement |
| MSA | Master Service Agreement | broad legal framework |
| SOW | Statement of Work | scope, deliverables, schedule |
| WO | Work Order | specific work item |
| NDA | Non-Disclosure Agreement | confidentiality |
| BPA | Business Partnership Agreement | partnership terms |
| ISA | Interconnection Security Agreement | kết nối hệ thống giữa tổ chức |
| DPA | Data Processing Agreement | xử lý personal data |
| AUP | Acceptable Use Policy | acceptable usage |

```text
SLA = service performance
SOW = what work will be done
NDA = keep secret
MSA = master contract framework
MOU = informal common understanding
MOA = stronger agreement
ISA = system interconnection
DPA = personal data processing
```

---

# 5.4 — Compliance and Privacy

## 5.4.1 Compliance là gì?

Compliance là tuân thủ:

- luật
- quy định
- industry standard
- policy nội bộ
- contractual requirement

| Regulation/Standard | Liên quan |
|---|---|
| GDPR | Personal data EU |
| HIPAA | Healthcare / PHI |
| PCI DSS | Payment card data |
| SOX | Public company financial reporting |
| GLBA | Financial institutions |
| FERPA | Education records |

## 5.4.2 Privacy Principles

| Principle | Meaning |
|---|---|
| Data minimization | Chỉ thu thập dữ liệu cần thiết |
| Purpose limitation | Chỉ dùng đúng mục đích |
| Consent | Có sự đồng ý khi cần |
| Retention limitation | Không giữ quá lâu |
| Right to access | Người dùng có quyền truy cập dữ liệu |
| Right to deletion | Quyền yêu cầu xóa |
| Data portability | Chuyển dữ liệu |
| Transparency | Minh bạch cách xử lý |

## 5.4.3 Data Types in Privacy

| Data Type | Meaning |
|---|---|
| PII | Personally Identifiable Information |
| PHI | Protected Health Information |
| PCI / Cardholder data | Dữ liệu thẻ thanh toán |
| Financial data | Dữ liệu tài chính |
| Sensitive personal data | Dữ liệu nhạy cảm |
| Anonymized data | Dữ liệu đã ẩn danh |
| Pseudonymized data | Dữ liệu thay định danh bằng pseudonym |

## 5.4.4 Data Sovereignty

Data sovereignty nghĩa là dữ liệu chịu luật của nơi nó được lưu/xử lý.

Ví dụ:

- dữ liệu công dân EU chịu GDPR
- cloud region ảnh hưởng compliance
- cross-border transfer cần điều kiện pháp lý

Nếu câu hỏi nhắc đến “data must remain in country/region” → data sovereignty / geographic restriction.

## 5.4.5 Data Retention and Legal Hold

| Term | Meaning |
|---|---|
| Data retention | Giữ dữ liệu trong thời gian quy định |
| Data deletion | Xóa khi hết thời hạn |
| Legal hold | Tạm giữ dữ liệu vì điều tra/kiện tụng |
| E-discovery | Tìm kiếm dữ liệu phục vụ pháp lý |

Nếu có legal hold thì không được xóa dữ liệu dù retention period đã hết.

---

# 5.5 — Audits and Assessments

## 5.5.1 Audit là gì?

Audit là kiểm tra để xác định tổ chức có tuân thủ yêu cầu không.

Có thể kiểm tra:

- policy
- access control
- logs
- change management
- vulnerability management
- compliance
- evidence

## 5.5.2 Internal vs External Audit

| Type | Meaning |
|---|---|
| Internal audit | Do tổ chức tự thực hiện |
| External audit | Do bên ngoài độc lập thực hiện |
| Third-party audit | Vendor/partner được audit |
| Regulatory audit | Audit theo cơ quan/quy định |

## 5.5.3 Attestation and Assurance

| Term | Meaning |
|---|---|
| Attestation | Xác nhận một điều là đúng |
| Assurance | Mức độ tin cậy vào control/process |
| Evidence | Bằng chứng hỗ trợ audit |
| Finding | Phát hiện trong audit |
| Remediation plan | Kế hoạch xử lý finding |

## 5.5.4 Assessment Types

| Assessment | Purpose |
|---|---|
| Risk assessment | Đánh giá rủi ro |
| Vulnerability assessment | Tìm lỗ hổng |
| Penetration test | Khai thác thử có kiểm soát |
| Compliance assessment | Kiểm tra tuân thủ |
| Security assessment | Đánh giá security posture |
| Privacy impact assessment | Đánh giá tác động privacy |

## 5.5.5 Penetration Test Report

Pentest report thường gồm:

- executive summary
- scope
- methodology
- findings
- severity
- evidence
- impact
- recommendations
- remediation priority

---

# 5.6 — Security Awareness and Training

## 5.6.1 Security Awareness là gì?

Security awareness giúp user nhận biết và tránh rủi ro bảo mật.

Mục tiêu:

- giảm phishing
- giảm social engineering
- cải thiện reporting
- tăng compliance
- xây dựng security culture

## 5.6.2 Training Topics

| Topic | Nội dung |
|---|---|
| Phishing awareness | Nhận biết email/link độc hại |
| Password hygiene | Dùng password manager, không reuse |
| MFA usage | Biết dùng MFA đúng |
| Data handling | Phân loại và xử lý dữ liệu |
| Clean desk | Không để tài liệu nhạy cảm |
| Reporting incidents | Báo cáo sự cố |
| Social engineering | Vishing, smishing, impersonation |
| Remote work | VPN, Wi-Fi, device security |
| BYOD | Thiết bị cá nhân |
| Insider threat | Nhận biết dấu hiệu rủi ro |

## 5.6.3 Training Methods

| Method | Meaning |
|---|---|
| Computer-based training | Học qua hệ thống |
| Phishing simulation | Mô phỏng phishing |
| Tabletop exercise | Thảo luận kịch bản |
| Role-based training | Đào tạo theo vai trò |
| Just-in-time training | Đào tạo ngay khi cần |
| New-hire training | Đào tạo nhân viên mới |
| Annual refresher | Ôn lại hằng năm |

## 5.6.4 Measuring Training Effectiveness

Cách đo:

- phishing click rate
- report rate
- quiz score
- incident reduction
- policy violation reduction
- training completion rate

Nếu hỏi “làm sao biết training có hiệu quả?” → dùng metrics, phishing simulation results, before/after comparison.

---

# Module 5 — PBQ Checklist

## Governance PBQ

Tìm keyword:

- high-level requirement → policy
- specific mandatory config → standard
- step-by-step → procedure
- recommendation → guideline
- temporary approved deviation → exception
- alternative control → compensating control

## Risk PBQ

Tìm keyword:

- Low/Medium/High → qualitative
- money/cost/formula → quantitative
- cyber insurance → transfer
- patch/MFA/firewall → mitigate
- stop doing activity → avoid
- accept remaining risk → accept
- risk after controls → residual risk

## BIA PBQ

Tìm keyword:

- how long service can be down → RTO
- how much data can be lost → RPO
- average repair time → MTTR
- average time between failures → MTBF
- business process priority → BIA

## Third-party PBQ

Tìm keyword:

- evaluate vendor before contract → due diligence
- monitor vendor after contract → vendor monitoring
- uptime/response time → SLA
- scope/deliverables/schedule → SOW
- broad contract framework → MSA
- confidentiality → NDA
- system connection between organizations → ISA
- pentest scope/rules → ROE

## Compliance/Privacy PBQ

Tìm keyword:

- payment card → PCI DSS
- healthcare → HIPAA
- EU personal data → GDPR
- financial reporting public company → SOX
- data must remain in region → data sovereignty
- keep data for lawsuit → legal hold
- collect only necessary data → data minimization

## Audit PBQ

Tìm keyword:

- independent review → external audit
- internal review → internal audit
- proof control works → evidence
- issue discovered → finding
- fix plan → remediation plan
- confirm claim is true → attestation

## Awareness PBQ

Tìm keyword:

- users clicking phishing → phishing awareness training
- training by job duties → role-based training
- test without impacting production → tabletop
- measure effectiveness → metrics/click rate/report rate
- new employee → new-hire training

---

# Module 5 — High Value Keywords

```text
Governance
Policy
Standard
Procedure
Guideline
Exception
Exemption
Compensating control
Risk acceptance
Data owner
Data controller
Data processor
Data custodian
Data steward
Risk management
Risk assessment
Qualitative
Quantitative
SLE
ARO
ALE
AV
EF
Risk appetite
Risk tolerance
Risk threshold
Residual risk
BIA
RTO
RPO
MTTR
MTBF
Risk register
Mitigate
Accept
Transfer
Avoid
Due care
Due diligence
Vendor monitoring
Questionnaire
Rules of engagement
SLA
MOU
MOA
MSA
SOW
WO
NDA
BPA
ISA
DPA
Compliance
Privacy
GDPR
HIPAA
PCI DSS
SOX
Data minimization
Purpose limitation
Consent
Data sovereignty
Data retention
Legal hold
E-discovery
Internal audit
External audit
Attestation
Assurance
Evidence
Finding
Remediation plan
Security awareness
Phishing simulation
Role-based training
Tabletop exercise
Metrics
```

---

# Module 5 — Câu hỏi tự kiểm tra nhanh

## Câu 1
Tài liệu cấp cao nói tổ chức phải bảo vệ PII là gì?

**Đáp án:** Policy.

## Câu 2
Tài liệu yêu cầu password tối thiểu 14 ký tự là gì?

**Đáp án:** Standard.

## Câu 3
Tài liệu hướng dẫn từng bước reset password là gì?

**Đáp án:** Procedure.

## Câu 4
Risk analysis dùng tiền và công thức ALE là loại gì?

**Đáp án:** Quantitative.

## Câu 5
Risk analysis dùng High/Medium/Low là loại gì?

**Đáp án:** Qualitative.

## Câu 6
Mua cyber insurance là risk strategy nào?

**Đáp án:** Transfer.

## Câu 7
Sau khi áp control, rủi ro còn lại gọi là gì?

**Đáp án:** Residual risk.

## Câu 8
Hệ thống được phép downtime tối đa bao lâu là chỉ số gì?

**Đáp án:** RTO.

## Câu 9
Dữ liệu được phép mất tối đa bao nhiêu thời gian là chỉ số gì?

**Đáp án:** RPO.

## Câu 10
Vendor được hỏi về DR plan và encryption trước khi ký hợp đồng là hoạt động gì?

**Đáp án:** Due diligence / questionnaire.

---

# Ưu tiên ôn Module 5 trước ngày thi

## Mức bắt buộc

1. Policy vs standard vs procedure vs guideline
2. Risk strategies: mitigate, accept, transfer, avoid
3. Qualitative vs quantitative risk
4. SLE, ARO, ALE
5. BIA, RTO, RPO, MTTR, MTBF
6. Due care vs due diligence
7. Third-party risk and vendor monitoring
8. Agreement types: SLA, MOU, MOA, MSA, SOW, NDA, ISA
9. Compliance and privacy: GDPR, HIPAA, PCI DSS, SOX
10. Data roles: owner, controller, processor, custodian/steward

## Mức nên biết thêm

1. Risk appetite/tolerance/threshold
2. Residual risk
3. Legal hold and e-discovery
4. Audit findings and remediation
5. Privacy principles
6. Awareness training metrics
7. Rules of engagement
8. Exceptions/exemptions

---

# Một trang nhớ nhanh

```text
Module 5 = governance + risk + compliance

Documents:
Policy = high-level rule
Standard = specific mandatory requirement
Procedure = step-by-step
Guideline = recommendation

Risk:
Qualitative = Low/Medium/High
Quantitative = money/numbers
SLE = AV x EF
ALE = SLE x ARO

Strategies:
Mitigate = reduce
Accept = live with it
Transfer = insurance/outsource
Avoid = stop activity

BIA:
RTO = maximum downtime
RPO = maximum data loss
MTTR = average repair time
MTBF = average time between failures

Third-party:
Due diligence = investigate before
Due care = act responsibly
SLA = uptime/response
SOW = scope/deliverables
NDA = confidentiality
ISA = system interconnection

Privacy:
GDPR = EU personal data
HIPAA = healthcare/PHI
PCI DSS = card data
SOX = public financial reporting
Legal hold = do not delete
Data sovereignty = data location law
```
