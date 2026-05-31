# Security+ SY0-701 — Module 4: Security Operations

> Mục tiêu: Đây là bản tổng hợp kiến thức cần học cho **Module 4 — Security Operations**.  
> Module này có tỷ trọng cao nhất trong bài thi SY0-701, khoảng **28%** tổng điểm, nên nên ưu tiên ôn kỹ.

---

## 0. Tổng quan Module 4

Module 4 tập trung vào **vận hành bảo mật thực tế**:

- Hardening hệ thống
- Quản lý tài sản
- Vulnerability management
- Security monitoring
- Firewall, secure protocols, email security
- IAM / MFA / password security
- Automation / orchestration
- Incident response
- Digital forensics
- Log analysis

Nếu Module 2 là “biết attacker làm gì”, thì Module 4 là “biết defender phải vận hành, phát hiện, phản ứng thế nào”.

---

# 4.1 — Apply Common Security Techniques to Computing Resources

## 4.1.1 Secure Baselines

### Khái niệm
Secure baseline là **cấu hình chuẩn an toàn ban đầu** cho hệ thống.

Ví dụ:
- Windows baseline
- Linux baseline
- CIS Benchmark
- Cloud security baseline
- Router/switch baseline

### Quy trình cần nhớ

```text
Establish → Deploy → Maintain
```

| Bước | Ý nghĩa |
|---|---|
| Establish | Tạo baseline chuẩn |
| Deploy | Áp dụng vào hệ thống |
| Maintain | Duy trì, cập nhật, kiểm tra lệch chuẩn |

### Keyword dễ gặp
- Secure baseline
- Configuration baseline
- Configuration drift
- Standard image
- Golden image
- CIS Benchmark

---

## 4.1.2 Hardening Targets

Hardening là giảm attack surface bằng cách tắt, gỡ, giới hạn, cập nhật hoặc cấu hình an toàn hơn.

### Các đối tượng cần hardening

| Target | Điểm cần nhớ |
|---|---|
| Mobile devices | MDM, encryption, screen lock, remote wipe |
| Workstations | Host firewall, EDR, patching, least privilege |
| Switches | Port security, disable unused ports, 802.1X |
| Routers | ACL, secure management, disable insecure protocols |
| Cloud infrastructure | IAM, security groups, logging, encryption |
| Servers | Patch, remove unnecessary services, hardening baseline |
| ICS/SCADA | Availability priority, segmentation, difficult to patch |
| Embedded systems | Limited resources, firmware updates |
| IoT devices | Default password, segmentation |
| RTOS | Real-time requirement, limited patching |

### Exam tip
Nếu câu hỏi nói hệ thống cũ, không thể patch, hoặc ICS/SCADA:
- dùng segmentation
- compensating controls
- monitoring
- isolation
- không tự ý reboot nếu ảnh hưởng availability

---

## 4.1.3 Wireless and Mobile Security

### Wireless installation considerations

| Term | Meaning |
|---|---|
| Site survey | Khảo sát vị trí, vật cản, tín hiệu |
| Heat map | Bản đồ vùng phủ sóng Wi-Fi |

### Mobile deployment models

| Model | Meaning |
|---|---|
| BYOD | Bring Your Own Device |
| COPE | Corporate-Owned, Personally Enabled |
| CYOD | Choose Your Own Device |

### Connection methods

- Cellular
- Wi-Fi
- Bluetooth

### Wireless security settings

| Term | Ý nghĩa |
|---|---|
| WPA3 | Chuẩn Wi-Fi bảo mật mới |
| SAE | Thay thế PSK handshake cũ trong WPA3 |
| 802.1X | Port-based network access control |
| EAP | Authentication framework |
| RADIUS | Centralized authentication server |

---

## 4.1.4 Application Security

Các keyword cần thuộc:

| Term | Meaning |
|---|---|
| Input validation | Kiểm tra dữ liệu đầu vào để chống injection |
| Secure cookies | Cookie có thuộc tính Secure, HttpOnly, SameSite |
| Static code analysis | Phân tích source code khi chưa chạy |
| Code signing | Ký mã để xác minh nguồn gốc và integrity |
| Sandboxing | Chạy app trong môi trường giới hạn |
| Monitoring | Theo dõi hành vi bất thường |

### Dễ nhầm
- SAST: phân tích code tĩnh.
- DAST: kiểm thử app khi đang chạy.
- Fuzzing: gửi input ngẫu nhiên để tìm crash/lỗi.

---

# 4.2 — Asset Management

## 4.2.1 Asset Lifecycle

Asset management là quản lý tài sản từ lúc mua đến lúc hủy.

```text
Acquisition → Assignment → Monitoring → Decommissioning → Disposal
```

| Giai đoạn | Ý nghĩa |
|---|---|
| Acquisition / Procurement | Mua hoặc tiếp nhận tài sản |
| Assignment / Accounting | Gán tài sản cho người dùng/bộ phận |
| Monitoring / Tracking | Theo dõi, inventory, enumeration |
| Decommissioning | Loại khỏi sử dụng |
| Disposal | Hủy, xóa, tiêu hủy an toàn |

---

## 4.2.2 Data Sanitization and Destruction

| Method | Ý nghĩa |
|---|---|
| Clearing | Xóa logic, có thể phục hồi bằng kỹ thuật nâng cao |
| Purging | Xóa mạnh hơn, khó phục hồi |
| Degaussing | Khử từ ổ đĩa từ tính |
| Shredding | Cắt nhỏ vật lý |
| Pulverizing | Nghiền nát |
| Incineration | Thiêu hủy |
| Certificate of destruction | Giấy xác nhận đã hủy |

### Exam tip
Nếu câu hỏi nhắc đến bên thứ ba tiêu hủy ổ cứng:
- cần **certificate of destruction**
- cần chain of custody nếu tài sản chứa dữ liệu nhạy cảm

---

## 4.2.3 Data Retention

Data retention là chính sách giữ dữ liệu trong bao lâu.

Cần nhớ:
- retention theo compliance
- retention theo business need
- purge/delete khi hết thời hạn
- không giữ dữ liệu lâu hơn cần thiết

---

# 4.3 — Vulnerability Management

## 4.3.1 Identification Methods

| Method | Ý nghĩa |
|---|---|
| Vulnerability scan | Quét lỗ hổng |
| Port scan | Xem dịch vụ/port đang mở |
| Static analysis | Phân tích source code |
| Dynamic analysis | Phân tích khi app đang chạy |
| Package monitoring | Kiểm tra package/dependency |
| Threat feed | Nguồn threat intelligence |
| Penetration testing | Mô phỏng tấn công |
| Bug bounty | Responsible disclosure program |
| Audit | Kiểm tra hệ thống/quy trình |

---

## 4.3.2 Threat Intelligence

| Type | Meaning |
|---|---|
| OSINT | Open-source intelligence |
| Proprietary / third-party | Threat intel trả phí hoặc từ vendor |
| Information-sharing organization | Tổ chức chia sẻ threat intel |
| Dark web intelligence | Theo dõi leak, credential, forum ngầm |

### Keyword dễ gặp
- IOC: Indicator of Compromise
- TTP: Tactics, Techniques, Procedures
- STIX: Format chia sẻ threat intel
- TAXII: Giao thức trao đổi threat intel

---

## 4.3.3 Penetration Testing

### Pentest vs Vulnerability Scan

| Vulnerability Scan | Penetration Test |
|---|---|
| Tìm lỗ hổng | Khai thác thử lỗ hổng |
| Ít xâm lấn | Có thể xâm lấn hơn |
| Tự động nhiều | Cần kỹ năng thủ công |
| Dùng để identify | Dùng để validate impact |

### Rules of Engagement

ROE xác định:
- scope
- thời gian test
- IP/domain trong phạm vi
- kỹ thuật được phép
- emergency contact
- dữ liệu nhạy cảm xử lý thế nào

---

## 4.3.4 Vulnerability Analysis

| Term | Meaning |
|---|---|
| False positive | Báo có lỗi nhưng thực tế không có |
| False negative | Không báo lỗi nhưng thực tế có lỗi |
| CVE | Mã định danh lỗ hổng |
| CVSS | Điểm mức độ nghiêm trọng |
| Exposure factor | Mức thiệt hại nếu bị khai thác |
| Risk tolerance | Mức rủi ro tổ chức chấp nhận |

### Ưu tiên xử lý lỗ hổng

Không chỉ dựa vào CVSS. Cần xem:
- có public exploit chưa
- asset có critical không
- exposure ra Internet không
- có compensating control không
- risk tolerance của tổ chức

---

## 4.3.5 Remediation and Validation

```text
Identify → Analyze → Prioritize → Remediate → Validate → Report
```

| Action | Ý nghĩa |
|---|---|
| Patching | Vá lỗi |
| Segmentation | Giới hạn phạm vi ảnh hưởng |
| Compensating control | Control thay thế khi chưa fix được |
| Exception | Chấp nhận ngoại lệ có phê duyệt |
| Rescanning | Quét lại sau khi sửa |
| Verification | Xác minh lỗi đã được xử lý |

---

# 4.4 — Security Alerting and Monitoring

## 4.4.1 Monitoring Activities

| Activity | Meaning |
|---|---|
| Log aggregation | Gom log về một nơi |
| Alerting | Cảnh báo khi có dấu hiệu bất thường |
| Scanning | Quét hệ thống |
| Reporting | Báo cáo |
| Archiving | Lưu trữ log |
| Quarantine | Cách ly đối tượng nguy hiểm |
| Alert tuning | Điều chỉnh rule để giảm false positive |

---

## 4.4.2 Tools

| Tool | Purpose |
|---|---|
| SIEM | Thu thập, phân tích, correlate log |
| Antivirus | Phát hiện malware truyền thống |
| EDR | Endpoint Detection and Response |
| XDR | Extended Detection and Response |
| DLP | Data Loss Prevention |
| NetFlow | Theo dõi metadata lưu lượng mạng |
| SNMP traps | Cảnh báo từ thiết bị mạng |
| Vulnerability scanner | Quét lỗ hổng |
| SCAP | Chuẩn tự động hóa kiểm tra cấu hình/lỗ hổng |
| Benchmarks | Baseline cấu hình an toàn |

### SIEM cần nhớ
SIEM dùng để:
- log aggregation
- correlation
- alerting
- incident investigation
- compliance reporting

---

# 4.5 — Modify Enterprise Capabilities to Enhance Security

## 4.5.1 Firewall

### Firewall rules cần nhớ

| Concept | Meaning |
|---|---|
| Rule order | Thứ tự rule rất quan trọng |
| First match wins | Match rule đầu tiên thì dừng |
| Implicit deny | Không match rule nào thì deny |
| Least privilege | Chỉ mở đúng port/source/destination cần thiết |
| Screened subnet | DMZ |

### Firewall PBQ format

| Source | Destination | Source Port | Destination Port | Protocol | Action |
|---|---|---|---|---|---|
| User subnet | Web server | Any | 443 | TCP | Allow |
| Any | Any | Any | Any | Any | Deny |

### Lỗi hay gặp
- Đặt allow any any ở đầu.
- Dùng `0.0.0.0/24` thay vì `0.0.0.0/0`.
- Mở port quá rộng.
- Nhầm protocol với service.
- Quên deny all cuối.

---

## 4.5.2 Web Filtering

| Method | Meaning |
|---|---|
| Agent-based | Cài agent trên endpoint |
| Centralized proxy | Proxy trung tâm |
| URL scanning | Kiểm tra URL |
| Content categorization | Phân loại nội dung |
| Reputation | Chặn dựa trên uy tín domain/IP |
| Block rules | Rule chặn cụ thể |

---

## 4.5.3 Operating System Security

| Control | Meaning |
|---|---|
| Group Policy | Quản lý cấu hình Windows tập trung |
| SELinux | Mandatory access control trên Linux |
| Host firewall | Firewall trên endpoint/server |
| File integrity monitoring | Theo dõi thay đổi file quan trọng |

---

## 4.5.4 Secure Protocols and Ports

| Protocol | Port | Purpose |
|---|---:|---|
| FTP | 20/21 | File transfer, insecure |
| SSH | 22 | Secure remote administration |
| SFTP | 22 | Secure file transfer over SSH |
| Telnet | 23 | Remote shell, insecure |
| SMTP | 25 | Mail transfer |
| DNS | 53 | Name resolution |
| DHCP | 67/68 | Dynamic IP assignment |
| HTTP | 80 | Web traffic |
| POP3 | 110 | Email retrieval |
| NTP | 123 | Time synchronization |
| IMAP | 143 | Email retrieval |
| SNMP | 161/162 | Network monitoring / traps |
| LDAP | 389 | Directory service |
| HTTPS | 443 | Secure web |
| SMB | 445 | Windows file sharing |
| Syslog | 514 | Logging |
| LDAPS | 636 | Secure LDAP |
| FTPS | 989/990 | FTP over TLS |
| IMAPS | 993 | Secure IMAP |
| POP3S | 995 | Secure POP3 |
| SQL Server | 1433 | Microsoft SQL Server |
| MySQL | 3306 | MySQL database |
| RDP | 3389 | Remote Desktop |
| SIP | 5060/5061 | VoIP signaling |

### Dễ hỏi
- SSH thay Telnet.
- HTTPS thay HTTP.
- SFTP khác FTPS.
- LDAPS là LDAP dùng TLS.
- IMAPS/POP3S là email retrieval bảo mật.

---

## 4.5.5 Email Security

| Term | Meaning |
|---|---|
| SPF | Xác định mail server nào được gửi mail cho domain |
| DKIM | Ký email bằng cryptographic signature |
| DMARC | Policy xử lý email fail SPF/DKIM |
| Gateway | Email security gateway lọc spam/malware/phishing |

### Cách nhớ
- SPF = sender allowed?
- DKIM = message signed?
- DMARC = what to do if failed?

---

## 4.5.6 Endpoint Security

| Tool | Purpose |
|---|---|
| EDR | Detect/respond trên endpoint |
| XDR | Mở rộng detection nhiều nguồn |
| DLP | Ngăn rò rỉ dữ liệu |
| NAC | Kiểm soát thiết bị vào mạng |
| UBA | Phân tích hành vi người dùng |
| DNS filtering | Chặn domain độc hại |

---

# 4.6 — Identity and Access Management

## 4.6.1 Account Lifecycle

```text
Provisioning → Permission Assignment → Review → De-provisioning
```

| Term | Meaning |
|---|---|
| Provisioning | Tạo tài khoản |
| De-provisioning | Vô hiệu hóa/xóa tài khoản |
| Permission assignment | Gán quyền |
| Attestation | Xác nhận quyền vẫn phù hợp |
| Identity proofing | Xác minh danh tính ban đầu |
| Federation | Tin cậy danh tính giữa tổ chức/hệ thống |
| SSO | Đăng nhập một lần |

---

## 4.6.2 Federation and SSO Protocols

| Protocol | Purpose |
|---|---|
| LDAP | Directory access |
| SAML | SSO phổ biến cho enterprise |
| OAuth | Authorization delegated access |
| OIDC | Authentication layer trên OAuth 2.0 |

### Dễ nhầm
- SAML: thường dùng cho enterprise SSO.
- OAuth: ủy quyền truy cập, không phải password sharing.
- LDAP: truy vấn directory.
- RADIUS: centralized network authentication.

---

## 4.6.3 Access Control Models

| Model | Meaning |
|---|---|
| DAC | Owner quyết định quyền |
| MAC | Quyền dựa trên classification/label |
| RBAC | Quyền dựa trên role |
| ABAC | Quyền dựa trên attribute |
| Rule-based | Quyền dựa trên rule |
| Time-of-day | Giới hạn theo thời gian |

### Exam tip
Nếu câu hỏi nói “user thuộc phòng ban/chức vụ” → RBAC.  
Nếu câu hỏi nói “location, device health, time, clearance” → ABAC.  
Nếu câu hỏi nói “top secret/secret/confidential” → MAC.

---

## 4.6.4 MFA

| Factor | Example |
|---|---|
| Something you know | Password, PIN |
| Something you have | Smart card, OTP token, phone |
| Something you are | Fingerprint, face |
| Somewhere you are | Location |
| Something you do | Behavior pattern |

### MFA mạnh hơn
- Password + smart card
- Password + biometric
- Security key + PIN

### Không phải MFA thật
- Password + PIN  
Vì cả hai đều là **something you know**.

---

## 4.6.5 Password Security

| Concept | Meaning |
|---|---|
| Length | Quan trọng hơn complexity quá mức |
| Reuse | Không dùng lại password |
| Expiration | Không đổi quá thường xuyên nếu không có lý do |
| Password manager | Lưu password an toàn |
| Passwordless | Dùng passkey, biometric, security key |
| Password vaulting | PAM lưu và quản lý credential đặc quyền |
| JIT permissions | Cấp quyền tạm thời |
| Ephemeral credentials | Credential sống ngắn hạn |

---

# 4.7 — Automation and Orchestration

## 4.7.1 Use Cases

| Use case | Meaning |
|---|---|
| User provisioning | Tự động tạo tài khoản |
| Resource provisioning | Tự động tạo cloud/server/resource |
| Guard rails | Ràng buộc an toàn tự động |
| Security groups | Tự động áp policy nhóm |
| Ticket creation | Tự tạo ticket khi alert |
| Escalation | Tự chuyển cấp xử lý |
| Enable/disable services | Tự bật/tắt dịch vụ |
| CI/CD testing | Kiểm thử trong pipeline |
| API integrations | Kết nối công cụ bằng API |

---

## 4.7.2 Benefits

- Tiết kiệm thời gian
- Giảm lỗi thao tác tay
- Enforce baseline
- Scale bảo mật tốt hơn
- Phản ứng nhanh hơn
- Workforce multiplier

### Cẩn thận
Automation sai có thể gây ảnh hưởng lớn. Luôn cần:
- approval
- testing
- rollback
- logging
- monitoring

---

# 4.8 — Incident Response

## 4.8.1 Incident Response Lifecycle

Chuỗi cần thuộc lòng:

```text
Preparation → Detection & Analysis → Containment → Eradication → Recovery → Lessons Learned
```

| Phase | Meaning |
|---|---|
| Preparation | Chuẩn bị plan, tool, contact, training |
| Detection & Analysis | Phát hiện và phân tích |
| Containment | Cô lập để giảm thiệt hại |
| Eradication | Loại bỏ nguyên nhân |
| Recovery | Khôi phục hoạt động |
| Lessons Learned | Rút kinh nghiệm, cải thiện |

---

## 4.8.2 Incident Planning

Cần có:
- IR plan
- Communication plan
- Contact list
- Escalation path
- Roles and responsibilities
- Tabletop exercise
- Playbooks

### Exam tip
Nếu câu hỏi hỏi “làm gì trước khi sự cố xảy ra”:
- preparation
- tabletop
- playbook
- communication plan

---

## 4.8.3 Digital Forensics

| Concept | Meaning |
|---|---|
| Chain of custody | Chuỗi kiểm soát bằng chứng |
| Legal hold | Giữ dữ liệu phục vụ pháp lý |
| Hashing evidence | Xác minh integrity bằng chứng |
| Order of volatility | Thu thập dữ liệu dễ mất trước |
| Disk image | Bản sao forensic |
| Write blocker | Ngăn thay đổi dữ liệu gốc |
| Timeline analysis | Phân tích dòng thời gian |
| Metadata | Dữ liệu mô tả file/event |

### Order of volatility — dễ nhớ

```text
CPU/cache → RAM → Network state → Disk → Logs/backups
```

---

## 4.8.4 Log Data

Các loại log cần biết:

| Log source | Purpose |
|---|---|
| Firewall logs | Allow/deny traffic |
| DNS logs | Domain resolution |
| Authentication logs | Login success/failure |
| Endpoint logs | Process, malware, file activity |
| Application logs | App errors and events |
| Web server logs | HTTP requests |
| Email logs | Mail flow, spam/phishing |
| VPN logs | Remote access |
| Cloud logs | IAM/API/storage/network activity |

### Dấu hiệu compromise trong log

- Failed login nhiều lần
- Successful login sau nhiều failed login
- Impossible travel
- New admin account
- Privilege escalation
- Large outbound transfer
- Missing logs
- Out-of-cycle logging
- Unusual PowerShell command
- Connection to known malicious IP/domain

---

# Module 4 — PBQ Checklist

## Firewall PBQ
Cần kiểm tra:
- source đúng chưa
- destination đúng chưa
- port đúng chưa
- protocol TCP/UDP đúng chưa
- rule order đúng chưa
- deny all cuối chưa
- có rule quá rộng không

## IAM PBQ
Cần kiểm tra:
- user có đúng role không
- permission theo least privilege chưa
- deprovision user cũ chưa
- MFA factor có thật sự khác loại không
- RBAC/ABAC/MAC/DAC có chọn đúng không

## Incident Response PBQ
Cần kiểm tra:
- đang ở phase nào
- hành động tiếp theo là gì
- containment trước eradication
- preserve evidence trước khi thay đổi lớn
- lessons learned sau recovery

## Log Analysis PBQ
Cần tìm:
- source IP
- username
- failed/success login
- new account
- privilege escalation
- lateral movement
- data exfiltration
- timestamp bất thường

---

# Module 4 — High Value Keywords

```text
Secure baseline
Hardening
Configuration drift
Golden image
MDM
BYOD
COPE
CYOD
WPA3
802.1X
EAP
RADIUS
Input validation
Code signing
Sandboxing
Asset inventory
Sanitization
Certificate of destruction
Vulnerability scan
SAST
DAST
Fuzzing
Threat intelligence
OSINT
CVE
CVSS
False positive
False negative
SIEM
DLP
EDR
XDR
NetFlow
SNMP trap
Firewall rule
ACL
Implicit deny
DMZ
SPF
DKIM
DMARC
NAC
RBAC
ABAC
PAM
JIT permissions
Passwordless
Automation
Orchestration
Incident response
Containment
Eradication
Recovery
Chain of custody
Order of volatility
```

---

# Module 4 — Câu hỏi tự kiểm tra nhanh

## Câu 1
Một vulnerability scanner báo lỗi nhưng sau khi kiểm tra thì hệ thống không có lỗi. Đây là gì?

**Đáp án:** False positive.

## Câu 2
Một nhân viên nghỉ việc. Hành động IAM quan trọng nhất là gì?

**Đáp án:** De-provisioning / disable account.

## Câu 3
Firewall có rule `allow any any` ở đầu. Vấn đề là gì?

**Đáp án:** Rule này match toàn bộ traffic, làm các rule bên dưới vô dụng.

## Câu 4
Email security control nào dùng để xác định server được phép gửi mail cho domain?

**Đáp án:** SPF.

## Câu 5
Trong incident response, sau containment là bước nào?

**Đáp án:** Eradication.

## Câu 6
Tool nào dùng để gom log và correlate alert?

**Đáp án:** SIEM.

## Câu 7
Password + PIN có phải MFA mạnh không?

**Đáp án:** Không. Cả hai đều là something you know.

## Câu 8
Nếu cần chứng minh bằng chứng số không bị thay đổi, dùng gì?

**Đáp án:** Hash.

## Câu 9
SFTP dùng port nào?

**Đáp án:** 22.

## Câu 10
Một hệ thống ICS không thể patch ngay. Mitigation hợp lý là gì?

**Đáp án:** Segmentation, monitoring, compensating controls.

---

# Ưu tiên ôn Module 4 trước ngày thi

## Mức bắt buộc
1. Incident response lifecycle
2. Firewall rule order / implicit deny
3. IAM / MFA / access control models
4. Secure protocols and ports
5. Vulnerability management flow
6. SIEM / EDR / DLP / XDR
7. Email security SPF/DKIM/DMARC
8. Digital forensics and chain of custody

## Mức nên biết thêm
1. Automation / orchestration
2. Asset lifecycle
3. MDM deployment models
4. Wireless hardening
5. SCAP / benchmarks
6. File integrity monitoring

---

# Một trang nhớ nhanh

```text
Module 4 = vận hành bảo mật

Hardening:
Disable unused services, patching, host firewall, EDR

Vulnerability:
Scan → Analyze → Prioritize → Remediate → Validate → Report

Monitoring:
SIEM, logs, alerts, NetFlow, SNMP, DLP, EDR/XDR

Firewall:
Top-down, first match wins, least privilege, implicit deny

IAM:
Provisioning, de-provisioning, RBAC, ABAC, MFA, PAM

Incident Response:
Preparation → Detection/Analysis → Containment → Eradication → Recovery → Lessons Learned

Forensics:
Preserve evidence, chain of custody, hash, order of volatility
```
