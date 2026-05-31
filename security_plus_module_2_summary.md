# Security+ SY0-701 — Module 2: Threats, Vulnerabilities, and Mitigations

> Mục tiêu: Đây là bản tổng hợp kiến thức cần học cho **Module 2 — Threats, Vulnerabilities, and Mitigations**.  
> Module này chiếm khoảng **22%** bài thi SY0-701, rất quan trọng cho câu hỏi nhận diện attack, IOC, malware, social engineering và mitigation.

---

## 0. Tổng quan Module 2

Module 2 tập trung vào:

- Threat actors: ai là người tấn công?
- Motivations: vì sao họ tấn công?
- Threat vectors: tấn công đi qua đường nào?
- Vulnerabilities: điểm yếu nằm ở đâu?
- Malicious activity: dấu hiệu nào cho thấy đang bị tấn công?
- Mitigation: giảm thiểu hoặc ngăn chặn bằng cách nào?

Nếu Module 4 là “defender vận hành thế nào”, thì Module 2 là “attacker tấn công thế nào và defender nhận biết ra sao”.

---

# 2.1 — Threat Actors and Motivations

## 2.1.1 Threat Actors

| Threat Actor | Ý nghĩa | Đặc điểm chính |
|---|---|---|
| Nation-state | Nhóm được nhà nước hỗ trợ | Rất tinh vi, nhiều tài nguyên |
| Organized crime | Tội phạm có tổ chức | Mục tiêu tài chính |
| Hacktivist | Tấn công vì chính trị/xã hội | Defacement, leak dữ liệu, DDoS |
| Insider threat | Người trong tổ chức | Có quyền truy cập hợp pháp |
| Unskilled attacker | Script kiddie | Dùng tool có sẵn |
| Shadow IT | Hệ thống/dịch vụ ngoài kiểm soát IT | Tăng rủi ro vì không được quản lý |

## 2.1.2 Attributes of Threat Actors

| Attribute | Ý nghĩa |
|---|---|
| Internal / External | Bên trong hay bên ngoài tổ chức |
| Resources / Funding | Mức tài nguyên, tiền, công cụ |
| Sophistication / Capability | Mức độ tinh vi, kỹ năng, năng lực |

### Cách nhớ nhanh

```text
Nation-state = high funding + high sophistication
Script kiddie = low skill + tools có sẵn
Insider = access hợp pháp + nguy hiểm vì biết hệ thống
Organized crime = financial gain
Hacktivist = political/social belief
```

## 2.1.3 Motivations

| Motivation | Ví dụ |
|---|---|
| Data exfiltration | Đánh cắp dữ liệu |
| Espionage | Gián điệp |
| Service disruption | Làm gián đoạn dịch vụ |
| Blackmail | Tống tiền |
| Financial gain | Kiếm tiền |
| Philosophical / political beliefs | Niềm tin chính trị/xã hội |
| Revenge | Trả thù |
| Disruption / chaos | Gây hỗn loạn |
| War | Chiến tranh mạng |
| Ethical | Kiểm thử hoặc báo cáo có trách nhiệm |

---

# 2.2 — Threat Vectors and Attack Surfaces

## 2.2.1 Threat Vector là gì?

Threat vector là **đường tấn công** mà attacker dùng để xâm nhập hoặc gây hại.

Ví dụ:
- Email phishing
- SMS smishing
- USB infected
- Open ports
- Default credentials
- Vulnerable software
- Supply chain vendor

## 2.2.2 Message-based Attacks

| Vector | Meaning |
|---|---|
| Email | Phishing, malware attachment |
| SMS | Smishing |
| Instant Messaging | Link độc hại qua chat |
| Voice Call | Vishing |

```text
Phishing = email
Smishing = SMS
Vishing = voice
```

## 2.2.3 Social Engineering

| Attack | Ý nghĩa |
|---|---|
| Phishing | Lừa qua email |
| Spear phishing | Phishing có mục tiêu cụ thể |
| Whaling | Nhắm vào lãnh đạo cấp cao |
| Vishing | Lừa qua điện thoại |
| Smishing | Lừa qua SMS |
| Pretexting | Dựng câu chuyện giả |
| Impersonation | Mạo danh |
| Business Email Compromise | Mạo danh email doanh nghiệp để lừa chuyển tiền/thông tin |
| Watering hole | Gài mã độc vào website nạn nhân hay truy cập |
| Brand impersonation | Giả mạo thương hiệu |
| Typosquatting | Đăng ký domain gần giống domain thật |
| Misinformation | Thông tin sai, có thể không cố ý |
| Disinformation | Thông tin sai có chủ ý |

## 2.2.4 Other Attack Surfaces

| Attack Surface | Ví dụ |
|---|---|
| File-based | File đính kèm malware |
| Image-based | QR code độc hại, steganography |
| Removable device | USB chứa malware |
| Vulnerable software | App chưa patch |
| Unsupported systems | OS/app hết hỗ trợ |
| Unsecure networks | Wi-Fi mở, Bluetooth |
| Open service ports | Port dịch vụ mở không cần thiết |
| Default credentials | admin/admin |
| Supply chain | Vendor/MSP bị compromise |

## 2.2.5 Supply Chain

Supply chain attack là tấn công qua:

- vendor
- supplier
- managed service provider
- software update
- hardware provider
- third-party service

### Mitigation

- Vendor risk management
- Code signing
- Software bill of materials
- Least privilege
- Network segmentation
- Monitoring third-party access
- Contract/security requirements

---

# 2.3 — Vulnerabilities

## 2.3.1 Vulnerability là gì?

Vulnerability là **điểm yếu** có thể bị khai thác.

Ví dụ:
- lỗi code
- cấu hình sai
- password mặc định
- firmware lỗi thời
- thiếu patch
- hệ thống hết hỗ trợ

## 2.3.2 Application Vulnerabilities

| Vulnerability | Ý nghĩa |
|---|---|
| Memory injection | Inject code vào memory process |
| Buffer overflow | Ghi vượt vùng nhớ |
| Race condition | Lỗi do timing/thứ tự xử lý |
| TOC/TOU | Time-of-check / Time-of-use |
| Malicious update | Update bị cài mã độc |

### Buffer Overflow

Dấu hiệu:
- app crash
- arbitrary code execution
- memory corruption

Mitigation:
- input validation
- memory-safe languages
- ASLR
- DEP
- patching

## 2.3.3 Web Vulnerabilities

| Vulnerability | Ý nghĩa |
|---|---|
| SQL Injection | Chèn SQL độc hại vào query |
| XSS | Chèn script chạy trên browser nạn nhân |
| Directory Traversal | Truy cập file ngoài thư mục được phép |
| Forgery | Giả mạo request hoặc identity |
| Replay | Gửi lại request/token cũ |

## 2.3.4 SQL Injection

Mục tiêu:
- bypass login
- đọc database
- sửa/xóa dữ liệu
- dump thông tin nhạy cảm

Keyword ví dụ:

```text
' OR '1'='1
```

Mitigation:
- Prepared statements
- Parameterized queries
- Input validation
- Least privilege DB account
- WAF

## 2.3.5 Cross-Site Scripting — XSS

Attacker chèn JavaScript độc hại vào website.

Hậu quả:
- steal cookies
- session hijacking
- redirect user
- deface content

Mitigation:
- Output encoding
- Input validation
- Content Security Policy
- Secure cookies
- HttpOnly cookies

## 2.3.6 Race Conditions

Race condition xảy ra khi kết quả phụ thuộc vào timing.

| Term | Meaning |
|---|---|
| Time of Check | Lúc kiểm tra điều kiện/quyền |
| Time of Use | Lúc sử dụng tài nguyên |

Nếu trạng thái thay đổi giữa lúc check và lúc use thì có thể bị exploit.

## 2.3.7 OS, Hardware, Virtualization, Cloud Vulnerabilities

| Type | Ví dụ |
|---|---|
| OS-based | Kernel bug, privilege escalation |
| Hardware | Firmware vulnerability, end-of-life device |
| Legacy | Thiết bị/app cũ không còn support |
| VM escape | Thoát khỏi VM ra hypervisor/host |
| Resource reuse | Dữ liệu cũ còn lại trong tài nguyên tái sử dụng |
| Cloud-specific | Public bucket, IAM misconfiguration |

## 2.3.8 Misconfiguration

Misconfiguration là lỗi rất hay thi.

Ví dụ:
- S3 bucket public
- firewall allow any any
- default password
- exposed RDP/SSH
- excessive IAM permissions
- missing encryption
- disabled logging

Mitigation:
- Secure baseline
- Configuration management
- Least privilege
- Automated compliance scan
- Change management
- Logging and alerting

## 2.3.9 Mobile Vulnerabilities

| Term | Meaning |
|---|---|
| Sideloading | Cài app ngoài store chính thức |
| Jailbreaking | Gỡ giới hạn bảo mật iOS |
| Rooting | Gỡ giới hạn bảo mật Android |
| Outdated OS | Thiếu patch |
| Malicious app | App độc hại |

## 2.3.10 Zero-day

Zero-day là lỗ hổng:
- chưa có patch
- vendor có thể chưa biết
- attacker có thể exploit trước khi có bản vá

Mitigation:
- Defense in depth
- EDR/XDR
- IPS
- WAF
- Least privilege
- Segmentation
- Threat intelligence
- Rapid patching khi có fix

---

# 2.4 — Indicators of Malicious Activity

## 2.4.1 Malware Types

| Malware | Ý nghĩa | Dấu hiệu |
|---|---|---|
| Virus | Gắn vào file/chương trình | Lây khi file chạy |
| Worm | Tự lây qua mạng | Nhiều kết nối, scan network |
| Trojan | Giả dạng phần mềm hợp pháp | Backdoor, payload ẩn |
| Ransomware | Mã hóa dữ liệu đòi tiền | File đổi extension, ransom note |
| Spyware | Theo dõi người dùng | Data exfiltration |
| Keylogger | Ghi phím bấm | Credential theft |
| Rootkit | Ẩn sâu trong hệ thống | Khó phát hiện |
| Logic bomb | Kích hoạt theo điều kiện | Chạy vào ngày/điều kiện cụ thể |
| Bloatware | Phần mềm thừa | Tốn tài nguyên, tăng attack surface |

## 2.4.2 Ransomware IOC

Dấu hiệu:
- files renamed
- unusual file extensions
- ransom note
- high disk activity
- shadow copy deletion
- SMB spreading
- encryption process
- user cannot access files

Hành động ưu tiên:

```text
Isolate host → Disable shared drives → Preserve evidence → Start IR plan
```

## 2.4.3 Network Attacks

| Attack | Ý nghĩa |
|---|---|
| DoS | Làm dịch vụ không sẵn sàng |
| DDoS | Nhiều nguồn tấn công cùng lúc |
| Reflected DDoS | Dùng bên thứ ba phản hồi về nạn nhân |
| Amplified DDoS | Khuếch đại traffic |
| DNS poisoning | Làm sai kết quả DNS |
| DNS tunneling | Dùng DNS để truyền dữ liệu/lệnh |
| On-path attack | Attacker đứng giữa đường truyền |
| Replay attack | Gửi lại dữ liệu/token cũ |
| Credential replay | Dùng lại credential/token đã lấy được |

## 2.4.4 Wireless Attacks

| Attack | Ý nghĩa |
|---|---|
| Evil twin | AP giả mạo giống Wi-Fi thật |
| Rogue AP | AP trái phép trong mạng |
| Deauthentication | Ép client rớt khỏi Wi-Fi |
| Jamming | Gây nhiễu tín hiệu |
| Bluejacking | Gửi message qua Bluetooth |
| Bluesnarfing | Trộm dữ liệu qua Bluetooth |
| RFID cloning | Sao chép thẻ RFID |

Mitigation:
- WPA3
- 802.1X
- Disable WPS
- Strong passphrase
- Wireless IDS
- Site survey
- Certificate-based authentication

## 2.4.5 Application Attacks

| Attack | Ý nghĩa |
|---|---|
| Injection | Chèn lệnh/code |
| Buffer overflow | Ghi vượt bộ nhớ |
| Replay | Gửi lại request cũ |
| Privilege escalation | Tăng quyền |
| Forgery | Giả mạo request/identity |
| Directory traversal | Truy cập file trái phép |

## 2.4.6 Cryptographic Attacks

| Attack | Ý nghĩa |
|---|---|
| Downgrade | Ép dùng phiên bản crypto yếu hơn |
| Collision | Hai input khác nhau tạo cùng hash |
| Birthday attack | Khai thác xác suất collision |

Mitigation:
- Disable weak protocols
- Use TLS 1.2/1.3
- Strong ciphers
- SHA-256 or better
- Certificate validation
- HSTS

## 2.4.7 Password Attacks

| Attack | Ý nghĩa |
|---|---|
| Brute force | Thử mọi khả năng |
| Dictionary | Thử từ trong wordlist |
| Password spraying | Một vài password phổ biến trên nhiều account |
| Credential stuffing | Dùng credential leak từ nơi khác |
| Rainbow table | Dùng bảng hash tính sẵn |

Cách phân biệt nhanh:

```text
Brute force = nhiều password trên một account
Password spraying = một password trên nhiều account
Credential stuffing = dùng username/password bị leak
```

Mitigation:
- MFA
- Account lockout
- Rate limiting
- Password manager
- Passwordless
- Monitor impossible travel
- Block known leaked passwords

## 2.4.8 Indicators of Compromise — IOC

| IOC | Có thể chỉ ra |
|---|---|
| Account lockout | Brute force/password spraying |
| Concurrent session usage | Credential compromise |
| Impossible travel | Account compromise |
| Resource consumption | Malware, crypto mining, DoS |
| Resource inaccessibility | DoS, ransomware |
| Missing logs | Attacker xóa dấu vết |
| Out-of-cycle logging | Log bất thường ngoài lịch |
| Blocked content | Web filter/DLP triggered |
| Published/documented | Dữ liệu bị leak công khai |

---

# 2.5 — Mitigation Techniques

## 2.5.1 Segmentation

Segmentation chia mạng thành nhiều vùng để giảm lateral movement.

Ví dụ:
- User VLAN
- Server VLAN
- Guest VLAN
- DMZ
- Management VLAN

Dùng khi:
- ransomware spreading
- guest không được vào LAN
- IoT phải tách khỏi server
- ICS/SCADA cần cô lập
- chưa patch được hệ thống

## 2.5.2 Access Control

| Control | Meaning |
|---|---|
| ACL | Cho phép/chặn theo rule |
| Permissions | Quyền trên file/app/resource |
| Least privilege | Chỉ cấp quyền tối thiểu |
| RBAC | Quyền theo vai trò |
| ABAC | Quyền theo thuộc tính |

## 2.5.3 Application Allow List

Application allow list nghĩa là:
- chỉ app được phê duyệt mới được chạy
- app ngoài danh sách bị chặn

| Allow list | Deny list |
|---|---|
| Chỉ cho cái tốt chạy | Chặn cái xấu đã biết |
| Bảo mật hơn | Dễ quản lý hơn |
| Có thể gây bất tiện | Có thể bỏ sót malware mới |

## 2.5.4 Isolation and Quarantine

| Term | Meaning |
|---|---|
| Quarantine | Cách ly đối tượng nghi nhiễm |
| Isolation | Tách biệt để giảm ảnh hưởng |

Ví dụ:
- isolate infected host
- quarantine malware file
- quarantine VLAN
- sandbox suspicious file
- isolate guest network

## 2.5.5 Patching

Patching là vá lỗi phần mềm/hệ thống.

Cần nhớ:
- test patch trước
- có maintenance window
- có rollback/backout plan
- ưu tiên patch theo risk
- validate sau patch

## 2.5.6 Encryption

| Mục tiêu | Control |
|---|---|
| Bảo vệ laptop mất cắp | Full disk encryption |
| Bảo vệ web traffic | TLS/HTTPS |
| Bảo vệ VPN | IPsec/TLS VPN |
| Bảo vệ backup | Backup encryption |

## 2.5.7 Monitoring

Tools:
- SIEM
- EDR/XDR
- IDS/IPS
- NetFlow
- DLP
- DNS logs
- Firewall logs

## 2.5.8 Configuration Enforcement

Đảm bảo hệ thống không lệch khỏi baseline.

Keyword:
- configuration drift
- baseline enforcement
- desired state configuration

## 2.5.9 Decommissioning

Khi loại bỏ tài sản:
- remove from inventory
- revoke credentials/certificates
- wipe/sanitize data
- remove DNS/firewall rules
- destroy storage if needed
- get certificate of destruction

## 2.5.10 Hardening Techniques

| Technique | Ý nghĩa |
|---|---|
| Encryption | Bảo vệ dữ liệu |
| Endpoint protection | Antivirus/EDR |
| Host-based firewall | Firewall trên máy |
| HIPS | Host-based Intrusion Prevention |
| Disable ports/protocols | Tắt thứ không cần |
| Change default passwords | Đổi mật khẩu mặc định |
| Remove unnecessary software | Giảm attack surface |

---

# Module 2 — PBQ Checklist

## Social Engineering PBQ

Tìm keyword:
- email → phishing
- SMS → smishing
- call → vishing
- fake story → pretexting
- CEO/CFO money transfer → BEC/whaling
- website user hay vào bị compromise → watering hole
- domain gần giống → typosquatting

## Vulnerability PBQ

Tìm keyword:
- `' OR '1'='1` → SQL injection
- `<script>` → XSS
- `../..` → directory traversal
- timing issue → race condition
- old system no support → legacy/EOL
- public bucket → cloud misconfiguration
- VM escapes host → virtualization vulnerability

## Malware PBQ

Tìm keyword:
- file encrypted/ransom note → ransomware
- self-spreading network → worm
- fake useful app → trojan
- hidden privileged malware → rootkit
- records keystrokes → keylogger
- date/time trigger → logic bomb

## Network Attack PBQ

Tìm keyword:
- many sources overwhelm service → DDoS
- third-party reflected traffic → reflected DDoS
- small query large response → amplification
- fake AP same SSID → evil twin
- attacker between client/server → on-path
- reuse captured token → replay

## Password Attack PBQ

Tìm keyword:
- many passwords one user → brute force
- common password many users → password spraying
- leaked credential reused → credential stuffing
- hash lookup table → rainbow table

## Mitigation PBQ

Chọn control:
- stop lateral movement → segmentation
- reduce permissions → least privilege
- suspicious file → quarantine/sandbox
- unknown malware → application allow list
- unpatched system → patching/compensating control
- sensitive data transfer → DLP/encryption
- default password → change password
- unnecessary service → disable service

---

# Module 2 — High Value Keywords

```text
Nation-state
Organized crime
Hacktivist
Insider threat
Shadow IT
Phishing
Smishing
Vishing
Pretexting
Impersonation
BEC
Watering hole
Typosquatting
Supply chain
Default credentials
Open service ports
SQL injection
XSS
Buffer overflow
Race condition
TOC/TOU
VM escape
Misconfiguration
Zero-day
Ransomware
Trojan
Worm
Spyware
Keylogger
Rootkit
Logic bomb
DDoS
Reflected attack
Amplified attack
DNS poisoning
DNS tunneling
Evil twin
Rogue AP
On-path attack
Replay attack
Privilege escalation
Downgrade attack
Collision
Birthday attack
Password spraying
Credential stuffing
Account lockout
Impossible travel
Missing logs
Resource consumption
Segmentation
ACL
Least privilege
Isolation
Patching
Application allow list
Hardening
```

---

# Module 2 — Câu hỏi tự kiểm tra nhanh

## Câu 1
Một nhân viên nhận SMS có link giả mạo ngân hàng. Đây là gì?

**Đáp án:** Smishing.

## Câu 2
Một website cho phép nhập `' OR '1'='1` để bypass login. Đây là gì?

**Đáp án:** SQL injection.

## Câu 3
Một malware tự lây từ máy này sang máy khác qua mạng. Đây là gì?

**Đáp án:** Worm.

## Câu 4
File bị đổi extension hàng loạt và có ransom note. Đây là gì?

**Đáp án:** Ransomware.

## Câu 5
Một attacker dùng password “Winter2026!” thử trên hàng trăm account. Đây là gì?

**Đáp án:** Password spraying.

## Câu 6
Một user đăng nhập từ Việt Nam và 10 phút sau đăng nhập từ Mỹ. IOC này là gì?

**Đáp án:** Impossible travel.

## Câu 7
Một attacker tạo Wi-Fi giả cùng tên với Wi-Fi công ty. Đây là gì?

**Đáp án:** Evil twin.

## Câu 8
Lỗ hổng chưa có bản vá được gọi là gì?

**Đáp án:** Zero-day.

## Câu 9
Control nào giảm lateral movement tốt nhất?

**Đáp án:** Segmentation.

## Câu 10
Một ứng dụng chỉ cho phần mềm đã phê duyệt được chạy. Đây là gì?

**Đáp án:** Application allow list.

---

# Ưu tiên ôn Module 2 trước ngày thi

## Mức bắt buộc

1. Social engineering types
2. Malware types and IOC
3. Password attacks
4. Web attacks: SQLi, XSS, directory traversal
5. Network attacks: DDoS, DNS, on-path, replay
6. Vulnerability types: misconfiguration, zero-day, legacy, VM escape
7. Mitigation: segmentation, least privilege, patching, isolation
8. Threat actors and motivations

## Mức nên biết thêm

1. Supply chain attacks
2. Wireless attacks
3. Cryptographic attacks
4. Race condition / TOC-TOU
5. Mobile vulnerabilities
6. Hardware/firmware vulnerabilities

---

# Một trang nhớ nhanh

```text
Module 2 = attacker + vulnerability + IOC + mitigation

Threat actors:
Nation-state, organized crime, hacktivist, insider, script kiddie

Social engineering:
Phishing=email, smishing=SMS, vishing=voice, pretexting=fake story

Web attacks:
SQLi=query abuse, XSS=script in browser, traversal=../ files

Malware:
Ransomware=encrypted files, worm=self-spread, trojan=fake app,
rootkit=hidden privilege, keylogger=keystrokes

Password:
Brute force=many passwords one account
Spraying=one password many accounts
Stuffing=leaked credentials

IOC:
Impossible travel, account lockout, missing logs,
resource consumption, concurrent sessions

Mitigation:
Segmentation, ACL, least privilege, patching,
isolation/quarantine, encryption, monitoring, hardening
```
