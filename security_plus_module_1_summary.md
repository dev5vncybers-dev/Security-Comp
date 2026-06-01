# Security+ SY0-701 — Module 1: General Security Concepts

> Mục tiêu: Đây là bản tổng hợp kiến thức cần học cho **Module 1 — General Security Concepts**.  
> Module này chiếm khoảng **12%** bài thi SY0-701. Tuy tỷ trọng không cao nhất, nhưng đây là nền tảng để hiểu các module còn lại: security controls, CIA, AAA, Zero Trust, change management, cryptography và PKI.

---

## 0. Tổng quan Module 1

Module 1 tập trung vào các khái niệm nền tảng:

- Security controls
- CIA triad
- Non-repudiation
- AAA
- Gap analysis
- Zero Trust
- Physical security
- Deception and disruption
- Change management
- Cryptography
- PKI
- Certificates
- Hashing
- Digital signatures
- Obfuscation

Nếu Module 2 là “attacker tấn công thế nào”, Module 3 là “thiết kế kiến trúc thế nào”, Module 4 là “vận hành bảo mật thế nào”, thì Module 1 là “ngôn ngữ nền tảng của security”.

---

# 1.1 — Security Controls

## 1.1.1 Security Control là gì?

Security control là biện pháp dùng để:

- ngăn chặn sự cố
- phát hiện sự cố
- giảm thiểu thiệt hại
- khôi phục sau sự cố
- hướng người dùng tuân thủ chính sách

Ví dụ:
- firewall
- antivirus
- security guard
- policies
- CCTV
- backup
- awareness training

## 1.1.2 Control Categories

| Category | Ý nghĩa | Ví dụ |
|---|---|---|
| Technical | Control bằng công nghệ/hệ thống | Firewall, EDR, encryption, ACL |
| Managerial | Control về quản lý/chính sách | Risk assessment, policy, procedure |
| Operational | Control do con người/quy trình thực hiện | Security guard, awareness training |
| Physical | Control bảo vệ vật lý | Lock, fence, badge reader, CCTV |

### Cách nhớ nhanh

```text
Technical = system
Managerial = management/policy
Operational = people/process
Physical = physical protection
```

## 1.1.3 Control Types

| Control Type | Ý nghĩa | Ví dụ |
|---|---|---|
| Preventive | Ngăn sự cố xảy ra | Firewall rule, door lock, MFA |
| Deterrent | Làm attacker chùn bước | Warning sign, guard presence |
| Detective | Phát hiện sự cố | SIEM alert, CCTV, IDS |
| Corrective | Sửa/khôi phục sau sự cố | Restore backup, patch after incident |
| Compensating | Control thay thế khi control chính chưa đủ | Extra monitoring, firewall rule thay cho patch tạm thời |
| Directive | Hướng dẫn/yêu cầu tuân thủ | Policy, procedure, posted instruction |

### Cách nhớ theo câu hỏi

| Nếu câu hỏi nói... | Chọn |
|---|---|
| “prevent access” | Preventive |
| “discourage” | Deterrent |
| “detect/log/alert” | Detective |
| “restore/fix after incident” | Corrective |
| “alternative control” | Compensating |
| “policy tells users what to do” | Directive |

## 1.1.4 Ví dụ phân loại nhanh

| Control | Category | Type |
|---|---|---|
| Firewall | Technical | Preventive |
| IDS | Technical | Detective |
| Backup restore | Technical/Operational | Corrective |
| Security policy | Managerial | Directive |
| Security guard | Operational/Physical | Deterrent/Preventive |
| CCTV | Physical | Detective |
| Warning banner | Technical/Managerial | Deterrent/Directive |
| Fence | Physical | Preventive/Deterrent |

---

# 1.2 — Fundamental Security Concepts

## 1.2.1 CIA Triad

CIA là nền tảng của bảo mật:

| Principle | Ý nghĩa | Ví dụ control |
|---|---|---|
| Confidentiality | Chỉ người được phép mới xem được dữ liệu | Encryption, access control |
| Integrity | Dữ liệu không bị sửa trái phép | Hashing, digital signature |
| Availability | Hệ thống/dữ liệu sẵn sàng khi cần | Redundancy, backup, failover |

### Cách nhớ

```text
Confidentiality = keep secret
Integrity = keep correct
Availability = keep running
```

## 1.2.2 Confidentiality

Mục tiêu:
- ngăn lộ dữ liệu
- ngăn unauthorized disclosure

Controls:
- encryption
- access control
- MFA
- least privilege
- data classification
- DLP

## 1.2.3 Integrity

Mục tiêu:
- đảm bảo dữ liệu không bị thay đổi trái phép
- phát hiện thay đổi

Controls:
- hashing
- digital signature
- file integrity monitoring
- checksums
- certificates

## 1.2.4 Availability

Mục tiêu:
- hệ thống hoạt động liên tục
- người dùng hợp lệ truy cập được khi cần

Controls:
- redundancy
- clustering
- load balancing
- backup
- UPS/generator
- DDoS protection
- patching

## 1.2.5 Non-repudiation

Non-repudiation nghĩa là **không thể phủ nhận hành động đã thực hiện**.

Trong security, non-repudiation cung cấp:

- proof of origin
- proof of integrity
- strong assurance of authenticity

### Ví dụ

| Tình huống | Non-repudiation bằng gì? |
|---|---|
| Ký hợp đồng số | Digital signature |
| Email ký bằng private key | Digital signature |
| Transaction log có integrity | Log + hash/signature |

```text
Non-repudiation = cannot deny
Digital signature = integrity + origin + non-repudiation
```

## 1.2.6 AAA

AAA gồm:

| Term | Meaning | Ví dụ |
|---|---|---|
| Identification | Claim identity | Username |
| Authentication | Prove identity | Password, MFA, certificate |
| Authorization | Determine permissions | RBAC, ACL |
| Accounting | Track activity | Logs, login time, commands used |

```text
Identification = who you claim to be
Authentication = prove it
Authorization = what you can access
Accounting = what you did
```

## 1.2.7 Authentication Factors

| Factor | Ví dụ |
|---|---|
| Something you know | Password, PIN |
| Something you have | Smart card, OTP token, phone |
| Something you are | Fingerprint, face |
| Somewhere you are | Location |
| Something you do | Typing pattern, behavior |

Không phải MFA thật:

```text
Password + PIN
```

Vì cả hai đều là **something you know**.

## 1.2.8 Authorization Models

| Model | Meaning |
|---|---|
| RBAC | Role-based access control |
| ABAC | Attribute-based access control |
| DAC | Owner quyết định quyền |
| MAC | Dựa trên classification/label |
| Rule-based | Dựa trên rule |
| Time-based | Dựa trên thời gian |

### Exam tip

| Keyword trong câu hỏi | Đáp án hay gặp |
|---|---|
| Job role / department | RBAC |
| Attribute / location / device / risk | ABAC |
| Owner grants permission | DAC |
| Secret / Top Secret / clearance | MAC |

## 1.2.9 Gap Analysis

Gap analysis là so sánh:

```text
Current state vs Desired state
```

Mục tiêu:
- biết hiện tại đang ở đâu
- biết mục tiêu cần đạt
- xác định khoảng cách
- đưa recommendation để cải thiện

## 1.2.10 Zero Trust

Zero Trust = không tin mặc định, luôn xác minh.

```text
Never trust, always verify
```

Nguyên tắc:
- verify explicitly
- least privilege
- assume breach
- continuous monitoring
- segmentation
- policy-based access

## 1.2.11 Zero Trust Components

| Component | Meaning |
|---|---|
| Subject/System | User, device, app, workload |
| Policy Enforcement Point | Nơi thực thi allow/deny |
| Policy Decision Point | Nơi ra quyết định |
| Policy Engine | Đánh giá policy |
| Policy Administrator | Cấp token/credential hoặc yêu cầu PEP allow/deny |
| Adaptive identity | Dựa trên nhiều tín hiệu rủi ro |
| Threat scope reduction | Giảm phạm vi tấn công |
| Policy-driven access control | Truy cập dựa trên policy |

```text
PEP = gatekeeper
Policy Engine = decision logic
Policy Administrator = tells PEP what to do
```

## 1.2.12 Physical Security

| Control | Purpose |
|---|---|
| Bollards | Chặn xe/ramming attack |
| Access control vestibule | Mantrap, kiểm soát từng người/nhóm |
| Fencing | Tạo perimeter |
| Video surveillance | Giám sát, ghi hình |
| Security guard | Kiểm tra, phản ứng, deterrent |
| Access badge | Kiểm soát ra vào |
| Lighting | Tăng visibility, giảm rủi ro |
| Sensors | Phát hiện chuyển động/áp lực/nhiệt |

## 1.2.13 Sensors

| Sensor | Ý nghĩa |
|---|---|
| Infrared | Phát hiện nhiệt/chuyển động |
| Pressure | Phát hiện áp lực |
| Microwave | Phát hiện chuyển động vùng rộng |
| Ultrasonic | Dùng sóng âm để phát hiện chuyển động |

## 1.2.14 Deception and Disruption

| Technology | Meaning |
|---|---|
| Honeypot | Hệ thống mồi nhử |
| Honeynet | Mạng gồm nhiều honeypot |
| Honeyfile | File mồi nhử |
| Honeytoken | Dữ liệu/token giả để phát hiện lộ lọt |

```text
Honeypot = fake system
Honeynet = fake network
Honeyfile = fake file
Honeytoken = fake data/credential
```

---

# 1.3 — Change Management

## 1.3.1 Change Management là gì?

Change management là quy trình quản lý thay đổi để tránh:

- downtime
- lỗi cấu hình
- mất dữ liệu
- security misconfiguration
- thay đổi không được phê duyệt

Ví dụ:
- upgrade firewall
- patch server
- change ACL
- modify switch port
- deploy new application

## 1.3.2 Business Processes Impacting Security Operation

| Term | Meaning |
|---|---|
| Approval process | Quy trình phê duyệt |
| Ownership | Ai chịu trách nhiệm thay đổi |
| Stakeholders | Ai bị ảnh hưởng/cần góp ý |
| Impact analysis | Phân tích ảnh hưởng |
| Test results | Kết quả test trước khi triển khai |
| Backout plan | Kế hoạch rollback |
| Maintenance window | Thời gian triển khai được phép |
| Standard operating procedure | Quy trình chuẩn |

### Exam tip

Nếu câu hỏi hỏi “trước khi thay đổi production cần gì?”:
- approval
- impact analysis
- testing
- backout plan
- maintenance window
- documentation

## 1.3.3 Technical Implications

| Term | Meaning |
|---|---|
| Allow list | Chỉ cho thứ được phê duyệt chạy |
| Deny list | Chặn thứ nằm trong danh sách xấu |
| Restricted activities | Giới hạn hành động được phép |
| Downtime | Thời gian dịch vụ không khả dụng |
| Service restart | Restart service/daemon |
| Application restart | Restart ứng dụng |
| Legacy applications | App cũ, khó thay đổi |
| Dependencies | Thành phần phụ thuộc lẫn nhau |

## 1.3.4 Documentation and Version Control

Cần cập nhật:
- network diagrams
- firewall rules
- policies
- procedures
- system inventory
- configuration files

Version control giúp:
- theo dõi thay đổi
- rollback
- audit
- biết ai sửa gì khi nào

---

# 1.4 — Cryptographic Solutions

## 1.4.1 PKI

PKI = Public Key Infrastructure.

PKI bao gồm:
- policies
- procedures
- hardware
- software
- people
- certificates
- CA
- CRL/OCSP
- key management

Mục tiêu:
- bind public key với identity
- tạo trust
- quản lý certificate lifecycle

## 1.4.2 Public Key and Private Key

| Key | Meaning |
|---|---|
| Public key | Có thể chia sẻ công khai |
| Private key | Phải giữ bí mật |

Dùng để encrypt:

```text
Bob encrypts with Alice's public key
Alice decrypts with Alice's private key
```

Dùng để ký:

```text
Alice signs with Alice's private key
Bob verifies with Alice's public key
```

## 1.4.3 Symmetric vs Asymmetric Encryption

| Symmetric | Asymmetric |
|---|---|
| Một shared key | Public/private key pair |
| Nhanh | Chậm hơn |
| Khó phân phối key | Dễ trao đổi hơn |
| Dùng cho bulk encryption | Dùng cho key exchange/signature |

| Type | Algorithms |
|---|---|
| Symmetric | AES, 3DES |
| Asymmetric | RSA, ECC |

### Exam tip

TLS thường dùng cả hai:
- asymmetric để trao đổi/thiết lập key
- symmetric để mã hóa session data

## 1.4.4 Key Exchange

Key exchange giải quyết câu hỏi:

```text
Làm sao chia sẻ key qua mạng không an toàn?
```

Cách làm:
- asymmetric encryption
- Diffie-Hellman
- ECDHE
- session key
- ephemeral keys

### Keyword
- ephemeral = temporary
- forward secrecy = lộ private key sau này không giải mã được session cũ

## 1.4.5 Encryption Levels

| Level | Meaning |
|---|---|
| Full-disk | Mã hóa toàn bộ disk |
| Partition | Mã hóa partition |
| File | Mã hóa file |
| Volume | Mã hóa volume |
| Database | Mã hóa database |
| Record | Mã hóa từng record/field |
| Transport/communication | Mã hóa khi truyền |

| Scenario | Best control |
|---|---|
| Laptop bị mất | Full-disk encryption |
| Web traffic | TLS/HTTPS |
| Database chứa PII | Database/record encryption |
| VPN site-to-site | IPsec |
| File nhạy cảm riêng lẻ | File encryption |

## 1.4.6 Key Length

Nguyên tắc:
- key dài hơn thường khó brute force hơn
- symmetric key thường ngắn hơn asymmetric key nhưng vẫn mạnh
- asymmetric cần key dài hơn vì toán học khác

Ví dụ:
- AES-128/256
- RSA 2048/3072+
- ECC key ngắn hơn RSA nhưng vẫn mạnh tương đương trong nhiều trường hợp

## 1.4.7 Cryptographic Tools

| Tool | Meaning |
|---|---|
| TPM | Chip bảo mật trên thiết bị, lưu key như BitLocker |
| HSM | Thiết bị phần cứng bảo vệ key quy mô lớn |
| Key Management System | Quản lý vòng đời key |
| Secure enclave | Vùng xử lý bảo mật tách biệt |

| TPM | HSM |
|---|---|
| Thường trên endpoint/device | Thường trong enterprise/datacenter/cloud |
| Lưu key local | Quản lý nhiều key, hiệu năng cao |
| Ví dụ BitLocker | Ví dụ CA key, payment key |

## 1.4.8 Obfuscation

Obfuscation làm dữ liệu/code khó hiểu hơn, nhưng không mạnh như encryption.

| Technique | Meaning |
|---|---|
| Steganography | Giấu dữ liệu trong file khác |
| Tokenization | Thay dữ liệu thật bằng token |
| Data masking | Che một phần dữ liệu |

| Masking | Tokenization |
|---|---|
| Che dữ liệu khi hiển thị | Thay dữ liệu bằng token |
| Ví dụ ****1234 | Token map về dữ liệu thật trong vault |
| Dùng cho display | Dùng nhiều trong payment/data protection |

## 1.4.9 Hashing

Hashing tạo fingerprint của dữ liệu.

Đặc điểm:
- one-way
- fixed length output
- dùng kiểm tra integrity
- thay đổi nhỏ ở input làm hash thay đổi lớn

Ví dụ:
- SHA-256
- SHA-384
- SHA-512

Dùng cho:
- integrity check
- password storage
- file verification
- digital signature workflow

## 1.4.10 Salting

Salt là giá trị random thêm vào password trước khi hash.

Mục tiêu:
- chống rainbow table
- hai user cùng password vẫn có hash khác nhau

```text
hash(password + salt)
```

## 1.4.11 Key Stretching

Key stretching làm brute force chậm hơn bằng cách lặp hash nhiều lần.

Ví dụ:
- PBKDF2
- bcrypt
- scrypt
- Argon2

```text
Salt = chống rainbow table
Key stretching = làm brute force chậm
```

## 1.4.12 Digital Signatures

Digital signature cung cấp:
- integrity
- authentication
- non-repudiation

Quy trình ký đơn giản:

```text
1. Hash message
2. Encrypt hash with sender private key
3. Send message + signature
4. Receiver verifies using sender public key
```

Digital signature không nhất thiết encrypt toàn bộ message. Nó thường ký hash của message.

## 1.4.13 Blockchain and Open Public Ledger

Blockchain:
- distributed ledger
- blocks linked by hashes
- tamper-evident
- decentralized validation

Open public ledger:
- ai cũng có thể xem giao dịch
- transparency cao
- privacy phụ thuộc thiết kế

## 1.4.14 Certificates

Certificate bind identity với public key.

Certificate thường chứa:
- subject
- public key
- issuer
- validity dates
- serial number
- digital signature của CA

## 1.4.15 Certificate Authorities

| Term | Meaning |
|---|---|
| CA | Certificate Authority, cấp/ký certificate |
| Root CA | CA gốc được tin cậy |
| Intermediate CA | CA trung gian |
| Third-party CA | CA công khai như DigiCert, Sectigo |
| Internal CA | CA nội bộ tổ chức |
| Self-signed certificate | Certificate tự ký |
| Root of trust | Điểm tin cậy gốc |

## 1.4.16 CSR, CRL, OCSP

| Term | Meaning |
|---|---|
| CSR | Certificate Signing Request |
| CRL | Certificate Revocation List |
| OCSP | Online Certificate Status Protocol |

```text
CSR = request certificate
CRL = list of revoked certificates
OCSP = real-time certificate status check
```

## 1.4.17 Certificate Types

| Type | Meaning |
|---|---|
| Wildcard certificate | Bảo vệ nhiều subdomain, ví dụ *.example.com |
| SAN certificate | Certificate có nhiều tên miền |
| Self-signed | Tự ký, không được public trust mặc định |
| Third-party certificate | Được CA tin cậy công khai ký |

---

# Module 1 — PBQ Checklist

## Security Control PBQ

Tìm keyword:
- block/prevent → preventive
- detect/log/alert → detective
- restore/fix → corrective
- discourage → deterrent
- alternative/temporary → compensating
- policy/instruction → directive

## CIA PBQ

Tìm keyword:
- disclosure/leak/read by unauthorized → confidentiality
- modified/tampered/hash/signature → integrity
- downtime/outage/access unavailable → availability

## AAA PBQ

Tìm keyword:
- username/claim → identification
- password/MFA/certificate → authentication
- permissions/role/access → authorization
- logs/activity/session time → accounting

## Zero Trust PBQ

Chọn:
- verify explicitly
- least privilege
- continuous monitoring
- policy engine
- PEP/PDP
- segmentation
- no implicit trust

## Physical Security PBQ

Chọn:
- vehicle blocking → bollards
- one person at a time → access control vestibule/mantrap
- perimeter → fence
- monitoring video → CCTV
- badge access → access badge
- motion/pressure detection → sensors

## Crypto PBQ

Tìm keyword:
- fast bulk encryption → symmetric/AES
- public/private key → asymmetric/RSA/ECC
- integrity check → hashing
- non-repudiation → digital signature
- certificate status → OCSP/CRL
- request cert → CSR
- hardware key storage endpoint → TPM
- enterprise key hardware → HSM
- hide data in image → steganography
- replace data with token → tokenization
- display partial data → masking

---

# Module 1 — High Value Keywords

```text
Security controls
Technical
Managerial
Operational
Physical
Preventive
Deterrent
Detective
Corrective
Compensating
Directive
CIA
Confidentiality
Integrity
Availability
Non-repudiation
AAA
Identification
Authentication
Authorization
Accounting
Gap analysis
Zero Trust
PEP
PDP
Policy Engine
Policy Administrator
Adaptive identity
Bollards
Access control vestibule
Fencing
CCTV
Access badge
Sensors
Honeypot
Honeynet
Honeyfile
Honeytoken
Change management
Approval process
Stakeholders
Impact analysis
Backout plan
Maintenance window
Version control
PKI
Public key
Private key
Symmetric encryption
Asymmetric encryption
Key exchange
AES
RSA
ECC
TPM
HSM
Key management system
Secure enclave
Steganography
Tokenization
Data masking
Hashing
Salting
Digital signature
Key stretching
Blockchain
Certificate
CA
CSR
CRL
OCSP
Self-signed
Wildcard certificate
Root of trust
```

---

# Module 1 — Câu hỏi tự kiểm tra nhanh

## Câu 1
Firewall rule chặn truy cập trái phép là control type nào?

**Đáp án:** Preventive.

## Câu 2
SIEM phát hiện login bất thường là control type nào?

**Đáp án:** Detective.

## Câu 3
Restore từ backup sau ransomware là control type nào?

**Đáp án:** Corrective.

## Câu 4
Hash dùng chủ yếu để bảo vệ nguyên tắc nào trong CIA?

**Đáp án:** Integrity.

## Câu 5
MFA thuộc phần nào của AAA?

**Đáp án:** Authentication.

## Câu 6
Role quyết định quyền truy cập của user. Đây là gì?

**Đáp án:** Authorization / RBAC.

## Câu 7
Fake password file dùng để phát hiện attacker là gì?

**Đáp án:** Honeyfile.

## Câu 8
Cần rollback nếu change fail. Tài liệu nào cần có?

**Đáp án:** Backout plan.

## Câu 9
Cần kiểm tra certificate có bị revoke chưa theo thời gian gần real-time. Dùng gì?

**Đáp án:** OCSP.

## Câu 10
Muốn chứng minh message không bị sửa và đúng người gửi. Dùng gì?

**Đáp án:** Digital signature.

---

# Ưu tiên ôn Module 1 trước ngày thi

## Mức bắt buộc

1. Security control categories and types
2. CIA triad
3. AAA
4. Non-repudiation
5. Zero Trust components
6. Physical security controls
7. Honeypot/honeynet/honeyfile/honeytoken
8. Change management flow
9. Symmetric vs asymmetric encryption
10. Hashing, salting, key stretching
11. Digital signatures
12. PKI, CA, CSR, CRL, OCSP

## Mức nên biết thêm

1. Gap analysis
2. Secure enclave
3. Blockchain/open public ledger
4. Key escrow
5. Wildcard certificates
6. Root of trust
7. Technical implications of change management
8. Version control

---

# Một trang nhớ nhanh

```text
Module 1 = security foundation

Controls:
Technical, Managerial, Operational, Physical
Preventive, Deterrent, Detective, Corrective, Compensating, Directive

CIA:
Confidentiality = prevent disclosure
Integrity = prevent/detect modification
Availability = keep systems running

AAA:
Identification = username
Authentication = prove identity
Authorization = permissions
Accounting = logs/activity

Zero Trust:
Never trust, always verify
PEP = gatekeeper
Policy Engine = decision logic

Physical:
Bollards block vehicles
Mantrap controls one person/group
CCTV detects/records
Sensors detect movement/pressure

Crypto:
Symmetric = fast, same key
Asymmetric = public/private key
Hash = integrity
Salt = chống rainbow table
Key stretching = slow brute force
Digital signature = integrity + origin + non-repudiation
PKI = certificates + CA + trust
CSR = request cert
CRL/OCSP = revocation check
```
