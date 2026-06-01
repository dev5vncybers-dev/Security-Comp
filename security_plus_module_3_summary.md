# Security+ SY0-701 — Module 3: Security Architecture

> Mục tiêu: Đây là bản tổng hợp kiến thức cần học cho **Module 3 — Security Architecture**.  
> Module này chiếm khoảng **18%** bài thi SY0-701, tập trung vào kiến trúc bảo mật, cloud, network infrastructure, data protection, resilience và recovery.

---

## 0. Tổng quan Module 3

Module 3 tập trung vào việc thiết kế kiến trúc bảo mật:

- Cloud architecture
- Shared responsibility
- Infrastructure as Code
- Containers, microservices, virtualization
- Network segmentation
- Security zones
- IDS/IPS, firewall, WAF, NGFW, UTM
- VPN, TLS, IPsec, SD-WAN, SASE
- Data classification and data protection
- High availability, backups, disaster recovery

Nếu Module 2 là “attacker tấn công thế nào”, Module 4 là “vận hành bảo mật thế nào”, thì Module 3 là “thiết kế hệ thống bảo mật thế nào cho đúng”.

---

# 3.1 — Security Implications of Architecture Models

## 3.1.1 Cloud Models

| Model | Ý nghĩa | Trách nhiệm chính |
|---|---|---|
| IaaS | Infrastructure as a Service | Khách hàng quản OS, app, data |
| PaaS | Platform as a Service | Khách hàng quản app và data |
| SaaS | Software as a Service | Khách hàng chủ yếu quản data/user/config |
| Hybrid cloud | Kết hợp on-prem + cloud | Phải quản kết nối, identity, policy |
| Multi-cloud | Dùng nhiều cloud provider | Tăng availability nhưng phức tạp quản trị |
| Private cloud | Cloud riêng cho tổ chức | Kiểm soát cao hơn |
| Public cloud | Cloud dùng chung hạ tầng provider | Scale tốt, phụ thuộc provider |

## 3.1.2 Shared Responsibility Matrix

Shared responsibility là mô hình phân chia trách nhiệm giữa cloud provider và customer.

```text
Provider = security OF the cloud
Customer = security IN the cloud
```

| Thành phần | Ai thường chịu trách nhiệm? |
|---|---|
| Physical datacenter | Provider |
| Physical server/storage/network | Provider |
| Hypervisor | Provider |
| Guest OS | Customer trong IaaS |
| Application | Customer |
| Data | Customer |
| Identity and access | Customer |
| Configuration | Customer |
| Encryption key management | Thường là Customer |

### Exam tip

Nếu câu hỏi hỏi “cloud provider chịu trách nhiệm gì?”:

- physical security
- datacenter
- hardware
- underlying infrastructure

Nếu hỏi “customer chịu trách nhiệm gì?”:

- data
- IAM
- permissions
- application configuration
- encryption choices

## 3.1.3 Hybrid Considerations

Hybrid cloud cần chú ý:

- secure connectivity giữa on-prem và cloud
- VPN / direct connect
- identity federation
- logging tập trung
- consistent policy
- data sovereignty
- latency
- complexity

## 3.1.4 Third-party Vendors

Khi dùng vendor/cloud provider cần đánh giá:

- compliance
- SLA
- data handling
- access control
- audit reports
- incident notification
- geographic location
- subcontractors
- shared responsibility

### Mitigation

- vendor risk assessment
- contract requirements
- right to audit
- security questionnaire
- data processing agreement
- monitoring vendor access

## 3.1.5 Infrastructure as Code — IaC

IaC là quản lý hạ tầng bằng code.

Ví dụ:

- Terraform
- CloudFormation
- Ansible
- Pulumi

### Lợi ích

- repeatable deployment
- version control
- automation
- consistency
- giảm lỗi thao tác tay

### Rủi ro

- misconfiguration được tự động nhân rộng
- secrets hardcoded trong code
- template public có lỗi
- thiếu review

### Controls

- code review
- secrets management
- scanning IaC templates
- version control
- least privilege
- change management

## 3.1.6 Serverless

Serverless là mô hình chạy code mà không quản server trực tiếp.

Ví dụ:

- AWS Lambda
- Azure Functions
- Google Cloud Functions

### Lợi ích

- scale nhanh
- không cần quản server
- trả phí theo mức dùng

### Rủi ro

- insecure function permissions
- dependency vulnerabilities
- logging không đầy đủ
- event trigger bị abuse
- cold start / availability issue

### Exam tip

Serverless không có nghĩa là “không có server”. Nó nghĩa là provider quản server.

## 3.1.7 Microservices

Microservices chia ứng dụng thành nhiều service nhỏ.

### Lợi ích

- scale từng service
- deploy độc lập
- fault isolation tốt hơn

### Rủi ro

- nhiều API hơn
- service-to-service authentication
- secrets management khó hơn
- network traffic nội bộ nhiều hơn
- monitoring phức tạp

### Controls

- API gateway
- mutual TLS
- service mesh
- least privilege
- centralized logging
- container security

## 3.1.8 Containerization

Container chạy app trong môi trường đóng gói.

Ví dụ:

- Docker
- Kubernetes
- container registry

### Lợi ích

- portability
- fast deployment
- resource efficient
- consistent environment

### Rủi ro

- vulnerable images
- privileged containers
- exposed secrets
- container escape
- insecure registry
- misconfigured Kubernetes

### Controls

- scan container images
- use minimal base images
- do not run as root
- sign images
- restrict privileges
- network policies
- secrets management
- patch images

## 3.1.9 Virtualization

Virtualization chạy nhiều VM trên một host.

| Term | Meaning |
|---|---|
| Hypervisor | Lớp quản lý VM |
| Type 1 hypervisor | Chạy trực tiếp trên hardware |
| Type 2 hypervisor | Chạy trên OS |
| VM escape | VM thoát ra host/hypervisor |
| Snapshot | Trạng thái VM tại một thời điểm |

### Rủi ro

- VM escape
- snapshot chứa dữ liệu nhạy cảm
- VM sprawl
- resource exhaustion
- insecure management interface

### Controls

- patch hypervisor
- isolate management network
- least privilege admin
- monitor VM inventory
- secure snapshots

## 3.1.10 Network Infrastructure Concepts

| Concept | Ý nghĩa |
|---|---|
| Physical isolation | Tách biệt vật lý |
| Air-gapped | Không kết nối mạng khác/Internet |
| Logical segmentation | Tách bằng VLAN, subnet, ACL, firewall |
| SDN | Software-defined networking |
| On-premises | Hạ tầng tại tổ chức |
| Centralized | Quản lý tập trung |
| Decentralized | Quản lý phân tán |

### Air-gap

Dùng cho:

- ICS/SCADA
- classified system
- high-security environment

Nhược điểm:

- khó cập nhật
- khó vận hành
- vẫn có rủi ro qua USB/supply chain

## 3.1.11 IoT, ICS, SCADA, Embedded, RTOS

| Term | Ý nghĩa | Điểm cần nhớ |
|---|---|---|
| IoT | Thiết bị thông minh kết nối mạng | Default password, khó patch |
| ICS | Industrial Control Systems | Ưu tiên availability/safety |
| SCADA | Giám sát và điều khiển công nghiệp | Critical infrastructure |
| Embedded systems | Hệ thống nhúng | Resource limited |
| RTOS | Real-time OS | Yêu cầu phản hồi đúng thời gian |

### Exam tip

Với ICS/SCADA:

- đừng ưu tiên reboot/patch ngay nếu gây downtime nguy hiểm
- nên dùng segmentation, monitoring, allow list, compensating controls
- availability và safety rất quan trọng

## 3.1.12 High Availability

High availability là thiết kế để hệ thống vẫn hoạt động khi có lỗi.

Kỹ thuật:

- redundancy
- clustering
- load balancing
- failover
- geographic dispersion
- multiple power/network paths

## 3.1.13 Architecture Considerations

| Consideration | Ý nghĩa |
|---|---|
| Availability | Dịch vụ luôn sẵn sàng |
| Resilience | Chịu lỗi và phục hồi |
| Cost | Chi phí triển khai/vận hành |
| Responsiveness | Tốc độ phản hồi |
| Scalability | Khả năng mở rộng |
| Ease of deployment | Dễ triển khai |
| Risk transference | Chuyển giao rủi ro |
| Ease of recovery | Dễ phục hồi |
| Patch availability | Có bản vá không |
| Inability to patch | Không thể vá |
| Power | Nguồn điện |
| Compute | Tài nguyên xử lý |

---

# 3.2 — Secure Enterprise Infrastructure

## 3.2.1 Device Placement

Device placement là đặt thiết bị đúng vị trí trong kiến trúc.

Ví dụ:

- firewall giữa Internet và DMZ
- WAF trước web app
- IDS ở TAP/SPAN port
- IPS inline
- proxy giữa user và Internet
- jump server trong management network

### Exam tip

Nếu thiết bị cần “block traffic”:

- đặt inline.

Nếu thiết bị chỉ “monitor/detect”:

- dùng TAP/SPAN/monitor port.

## 3.2.2 Security Zones

Security zones chia mạng theo mức tin cậy.

| Zone | Ví dụ |
|---|---|
| Untrusted | Internet |
| DMZ | Public web/mail server |
| Internal | User LAN |
| Restricted | Database, finance, HR |
| Management | Admin/jump server |
| Guest | Guest Wi-Fi |

### Rule mẫu

```text
Internet → DMZ web: allow HTTPS
Internet → Internal: deny
User LAN → DB: deny direct
Web server → DB: allow required port only
Guest → Internal: deny
```

## 3.2.3 Attack Surface

Attack surface là tổng các điểm có thể bị tấn công.

Giảm attack surface bằng:

- close unused ports
- remove unnecessary software
- disable services
- patch systems
- least privilege
- segmentation
- application allow list
- secure configuration

## 3.2.4 Connectivity

Khi thiết kế connectivity cần xem:

- ai cần truy cập ai?
- port/protocol nào cần thiết?
- có cần VPN không?
- có cần encryption không?
- có cần segmentation không?
- logging/monitoring ở đâu?

## 3.2.5 Failure Modes

| Mode | Meaning | Security implication |
|---|---|---|
| Fail-open | Khi lỗi thì cho phép traffic qua | Availability cao hơn, security thấp hơn |
| Fail-closed | Khi lỗi thì chặn traffic | Security cao hơn, có thể gây downtime |

### Exam tip

- Safety/availability critical có thể cần fail-open.
- Security critical access control thường cần fail-closed.

## 3.2.6 Active vs Passive, Inline vs TAP

| Concept | Meaning |
|---|---|
| Active | Có thể tác động/block |
| Passive | Chỉ quan sát |
| Inline | Traffic đi xuyên qua thiết bị |
| TAP / Monitor | Copy traffic để quan sát |

Ví dụ:

- IDS thường passive/TAP.
- IPS thường active/inline.

## 3.2.7 Jump Server

Jump server là máy trung gian để admin truy cập hệ thống quan trọng.

### Lợi ích

- kiểm soát admin access
- central logging
- giảm exposure
- dùng MFA
- không mở SSH/RDP trực tiếp ra Internet

### Best practice

- đặt trong management network
- bắt buộc MFA
- log session
- least privilege
- restrict source IP

## 3.2.8 Proxy Server

Proxy là máy trung gian giữa client và server.

| Type | Ý nghĩa |
|---|---|
| Forward proxy | Đại diện cho client đi Internet |
| Reverse proxy | Đại diện cho server nhận request |
| Transparent proxy | Proxy không cần client cấu hình rõ |
| Authenticated proxy | Yêu cầu user login |

### Dùng để

- web filtering
- caching
- logging
- TLS inspection
- DLP
- malware scanning

## 3.2.9 IDS vs IPS

| IDS | IPS |
|---|---|
| Intrusion Detection System | Intrusion Prevention System |
| Detect/alert | Detect + block |
| Thường passive | Thường inline |
| Ít ảnh hưởng traffic | Có thể gây latency/fail-close |

### Detection methods

- signature-based
- anomaly-based
- behavior-based
- heuristic

## 3.2.10 Load Balancer

Load balancer phân phối traffic giữa nhiều server.

### Lợi ích

- high availability
- scalability
- failover
- health checks
- TLS termination

### Dễ hỏi

- load balancing khác clustering.
- load balancer phân phối request.
- clustering làm nhiều node hoạt động như một hệ thống/nhóm.

## 3.2.11 Sensors

Sensors thu thập dữ liệu từ network/host/environment.

Ví dụ:

- IDS sensor
- network sensor
- environmental sensor
- endpoint telemetry agent

## 3.2.12 Port Security

Port security bảo vệ switch port.

### Các kỹ thuật

- disable unused ports
- MAC address limiting
- sticky MAC
- 802.1X
- VLAN assignment
- DHCP snooping
- BPDU Guard
- Dynamic ARP Inspection

## 3.2.13 802.1X, EAP, RADIUS

| Term | Meaning |
|---|---|
| 802.1X | Port-based network access control |
| Supplicant | Client xin truy cập |
| Authenticator | Switch/AP kiểm soát cổng |
| Authentication server | RADIUS server |
| EAP | Framework xác thực |

### Flow đơn giản

```text
Client → Switch/AP → RADIUS → Allow/Deny network access
```

## 3.2.14 Firewall Types

| Firewall | Ý nghĩa |
|---|---|
| Packet filtering | Lọc theo IP/port/protocol |
| Stateful firewall | Theo dõi trạng thái session |
| Stateless firewall | Không theo dõi session |
| NGFW | App awareness, IPS, user awareness |
| WAF | Bảo vệ web application |
| UTM | Nhiều tính năng trong một thiết bị |
| Layer 4 firewall | Dựa trên IP/port/TCP/UDP |
| Layer 7 firewall | Dựa trên application/content |

### WAF vs NGFW

| WAF | NGFW |
|---|---|
| Bảo vệ web app | Bảo vệ network/app traffic rộng hơn |
| Chống SQLi/XSS | App control, IPS, URL filtering |
| Thường đặt trước web server | Đặt ở perimeter/internal segmentation |

## 3.2.15 Secure Communication and Access

### VPN

VPN tạo tunnel mã hóa qua mạng không tin cậy.

| Type | Use |
|---|---|
| Remote access VPN | User từ xa vào công ty |
| Site-to-site VPN | Kết nối hai site |
| Split tunnel | Chỉ traffic công ty đi VPN |
| Full tunnel | Toàn bộ traffic đi VPN |

### Split tunnel

Ưu điểm:

- giảm tải VPN
- tiết kiệm bandwidth

Rủi ro:

- user vừa vào corporate vừa ra Internet trực tiếp
- cần endpoint security tốt

## 3.2.16 TLS

TLS bảo vệ data in transit.

Dùng trong:

- HTTPS
- LDAPS
- SMTPS
- IMAPS
- POP3S
- VPN SSL/TLS

TLS cung cấp:

- confidentiality
- integrity
- authentication server bằng certificate

## 3.2.17 IPsec

IPsec dùng để bảo vệ IP traffic, hay gặp trong site-to-site VPN.

| Component | Meaning |
|---|---|
| AH | Authentication Header, integrity/authentication, không mã hóa payload |
| ESP | Encapsulating Security Payload, mã hóa + integrity |
| IKE | Internet Key Exchange |
| Tunnel mode | Mã hóa toàn bộ packet gốc |
| Transport mode | Chỉ bảo vệ payload |

### Cách nhớ

- ESP = encryption.
- AH = authentication/integrity.
- IKE = key exchange.

## 3.2.18 SD-WAN

SD-WAN quản lý WAN bằng software.

Lợi ích:

- chọn đường truyền tốt nhất
- centralized policy
- tối ưu cloud connectivity
- dùng nhiều link Internet/MPLS/LTE
- cải thiện resilience

## 3.2.19 SASE

SASE = Secure Access Service Edge.

Kết hợp:

- networking
- security
- cloud-delivered access

Các thành phần hay gặp:

- SWG
- CASB
- ZTNA
- FWaaS
- DLP

Ý chính: SASE giúp user ở bất kỳ đâu truy cập tài nguyên an toàn theo identity, policy và context.

---

# 3.3 — Data Protection Concepts and Strategies

## 3.3.1 Data Types

| Data Type | Ví dụ |
|---|---|
| Regulated data | PCI, HIPAA, GDPR-related |
| Trade secret | Bí mật kinh doanh |
| Intellectual property | Source code, design, patent |
| Legal information | Contract, legal case |
| Financial information | Bank, tax, payment |
| Human-readable | Text, document |
| Non-human-readable | Binary, encoded, machine data |

## 3.3.2 Data Classifications

| Classification | Ý nghĩa |
|---|---|
| Public | Công khai |
| Private | Cá nhân/nội bộ |
| Sensitive | Nhạy cảm |
| Confidential | Bảo mật |
| Restricted | Giới hạn nghiêm ngặt |
| Critical | Cực kỳ quan trọng cho hoạt động |

### Exam tip

Không có một thứ tự universal tuyệt đối giữa các label. Hãy đọc theo policy trong câu hỏi.

## 3.3.3 Data States

| State | Meaning | Control |
|---|---|---|
| Data at rest | Dữ liệu đang lưu trữ | Disk/database/file encryption |
| Data in transit | Dữ liệu đang truyền | TLS, VPN, IPsec |
| Data in use | Dữ liệu đang được xử lý | Access control, secure enclave, DLP, memory protection |

```text
At rest = stored
In transit = moving
In use = being processed
```

## 3.3.4 Data Sovereignty and Geolocation

Data sovereignty nghĩa là dữ liệu chịu luật của nơi dữ liệu được lưu trữ/xử lý.

Cần chú ý:

- country/region của cloud storage
- legal requirements
- cross-border transfer
- privacy regulations
- geolocation restrictions

## 3.3.5 Methods to Secure Data

| Method | Purpose |
|---|---|
| Geographic restrictions | Giới hạn vùng lưu/truy cập dữ liệu |
| Encryption | Bảo vệ confidentiality |
| Hashing | Kiểm tra integrity |
| Masking | Che một phần dữ liệu |
| Tokenization | Thay dữ liệu thật bằng token |
| Obfuscation | Làm dữ liệu khó hiểu hơn |
| Segmentation | Tách dữ liệu/hệ thống |
| Permission restrictions | Giới hạn quyền truy cập |

## 3.3.6 Masking vs Tokenization vs Encryption

| Method | Reversible? | Use case |
|---|---|---|
| Masking | Thường không hoặc chỉ che hiển thị | Che số thẻ: **** **** **** 1234 |
| Tokenization | Có thể map ngược qua token vault | Payment systems |
| Encryption | Có thể giải mã bằng key | Data at rest/in transit |

### Cách nhớ

- Masking = che.
- Tokenization = thay bằng token.
- Encryption = mã hóa bằng key.

---

# 3.4 — Resilience and Recovery

## 3.4.1 High Availability

High availability giúp giảm downtime.

Kỹ thuật:

- load balancing
- clustering
- failover
- redundant hardware
- redundant power
- multiple network links

## 3.4.2 Load Balancing vs Clustering

| Load Balancing | Clustering |
|---|---|
| Phân phối request | Nhiều node cùng hỗ trợ dịch vụ |
| Tập trung traffic distribution | Tập trung high availability |
| Dùng health checks | Có failover giữa node |

## 3.4.3 Site Considerations

| Site | Meaning | Recovery speed | Cost |
|---|---|---|---|
| Hot site | Đầy đủ hệ thống, gần như sẵn sàng chạy | Nhanh nhất | Cao nhất |
| Warm site | Có phần hạ tầng, cần cấu hình/restore thêm | Trung bình | Trung bình |
| Cold site | Chỉ có địa điểm/cơ sở cơ bản | Chậm nhất | Thấp nhất |

```text
Hot = sẵn sàng nhất
Cold = rẻ nhất nhưng chậm nhất
Warm = ở giữa
```

## 3.4.4 Geographic Dispersion

Geographic dispersion là phân tán hệ thống qua nhiều vùng địa lý.

Lợi ích:

- giảm rủi ro thiên tai/khu vực
- tăng availability
- hỗ trợ disaster recovery

Rủi ro:

- latency
- data sovereignty
- cost
- replication complexity

## 3.4.5 Platform Diversity and Multi-cloud

### Platform diversity

Dùng nhiều nền tảng khác nhau để tránh single point of failure.

### Multi-cloud

Dùng nhiều cloud provider.

Lợi ích:

- giảm vendor lock-in
- tăng resilience
- tránh phụ thuộc một provider

Nhược điểm:

- phức tạp IAM/logging/networking
- chi phí cao
- khó chuẩn hóa security policy

## 3.4.6 Continuity of Operations

COOP là kế hoạch duy trì hoạt động khi có sự cố.

Liên quan:

- BCP: Business Continuity Plan
- DRP: Disaster Recovery Plan
- Incident Response Plan
- communication plan
- alternate site
- backups

## 3.4.7 Capacity Planning

Capacity planning đảm bảo đủ tài nguyên cho hiện tại và tương lai.

Cần xem:

- people
- technology
- infrastructure
- compute
- storage
- bandwidth
- power
- licensing

## 3.4.8 Recovery Testing

| Test Type | Meaning |
|---|---|
| Tabletop exercise | Thảo luận kịch bản |
| Simulation | Mô phỏng thực tế hơn |
| Failover test | Kiểm tra chuyển sang hệ thống dự phòng |
| Parallel processing | Chạy song song hệ thống mới/cũ |

### Exam tip

Tabletop là ít xâm lấn nhất, thường dùng để kiểm tra plan mà không ảnh hưởng production.

## 3.4.9 Backups

| Backup Concept | Meaning |
|---|---|
| Onsite backup | Backup tại chỗ |
| Offsite backup | Backup ở địa điểm khác |
| Frequency | Tần suất backup |
| Encryption | Mã hóa backup |
| Snapshot | Ảnh chụp trạng thái tại thời điểm |
| Replication | Sao chép dữ liệu sang nơi khác |
| Journaling | Ghi lại thay đổi để recovery |
| Recovery | Khôi phục dữ liệu/hệ thống |

### Backup strategy

```text
3-2-1 rule:
3 copies
2 different media
1 offsite
```

### Ransomware backup best practice

- offline/immutable backup
- test restore
- separate credentials
- monitor backup deletion
- encrypt backup
- keep offsite copy

## 3.4.10 Power Resiliency

| Control | Meaning |
|---|---|
| UPS | Cấp điện tạm thời khi mất điện |
| Generator | Cấp điện lâu hơn |
| Dual power supply | Nguồn kép |
| Redundant circuits | Mạch điện dự phòng |
| PDU | Power distribution unit |

```text
UPS = ngắn hạn, đủ để shutdown hoặc chờ generator
Generator = dài hạn hơn
```

---

# Module 3 — PBQ Checklist

## Architecture PBQ

Kiểm tra:

- system đặt đúng zone chưa?
- Internet có vào trực tiếp internal không?
- DB có bị expose không?
- có DMZ cho public server không?
- có segmentation không?
- có jump server cho admin không?
- có logging/monitoring không?

## Cloud PBQ

Tìm keyword:

- customer misconfigured bucket → customer responsibility
- physical datacenter → provider responsibility
- IAM permissions → customer responsibility
- hybrid cloud → VPN/direct connection/federation
- IaC template → scan/review/version control
- serverless → function permissions/dependencies/logging

## Network Appliance PBQ

Chọn thiết bị:

- SQLi/XSS web app → WAF
- malware/network signature block → IPS
- detect only → IDS
- user web filtering → proxy/SWG
- admin remote management → jump server
- distribute traffic → load balancer
- remote secure access → VPN
- centralized network auth → RADIUS/802.1X

## Firewall PBQ

Cần nhớ:

- firewall rule top-down
- first match wins
- implicit deny
- least privilege
- source/destination/port/protocol đúng
- DMZ public server không nên có direct internal access
- Web server to DB chỉ mở port cần thiết

## VPN/IPsec PBQ

Tìm keyword:

- site-to-site → IPsec VPN
- remote user → remote access VPN
- encryption + integrity IP traffic → ESP
- authentication/integrity only → AH
- key exchange → IKE
- full packet protected → tunnel mode
- payload protected → transport mode

## Data Protection PBQ

Chọn control:

- data at rest → encryption
- data in transit → TLS/VPN/IPsec
- integrity → hashing
- hide display value → masking
- replace sensitive value → tokenization
- location law issue → data sovereignty/geographic restriction
- too much access → permission restriction/least privilege

## Recovery PBQ

Chọn giải pháp:

- fastest recovery site → hot site
- cheapest recovery site → cold site
- middle option → warm site
- short power outage → UPS
- long power outage → generator
- test plan without impacting production → tabletop
- ransomware backup → offline/immutable backup
- high availability web traffic → load balancer

---

# Module 3 — High Value Keywords

```text
Cloud
IaaS
PaaS
SaaS
Shared responsibility
Hybrid cloud
Multi-cloud
Infrastructure as Code
Serverless
Microservices
Containerization
Virtualization
VM escape
Air-gapped
Logical segmentation
SDN
IoT
ICS
SCADA
RTOS
Embedded systems
High availability
Security zones
DMZ
Attack surface
Fail-open
Fail-closed
Inline
TAP
Jump server
Proxy
IDS
IPS
Load balancer
Port security
802.1X
EAP
RADIUS
WAF
NGFW
UTM
Layer 4
Layer 7
VPN
TLS
IPsec
AH
ESP
IKE
Tunnel mode
Transport mode
SD-WAN
SASE
Data at rest
Data in transit
Data in use
Data sovereignty
Masking
Tokenization
Encryption
Hashing
Hot site
Warm site
Cold site
Geographic dispersion
Failover
Snapshot
Replication
Journaling
UPS
Generator
```

---

# Module 3 — Câu hỏi tự kiểm tra nhanh

## Câu 1
Trong cloud, ai chịu trách nhiệm bảo vệ dữ liệu và IAM configuration?

**Đáp án:** Customer.

## Câu 2
Thiết bị nào phù hợp nhất để chặn SQL injection và XSS trước web server?

**Đáp án:** WAF.

## Câu 3
IDS và IPS khác nhau thế nào?

**Đáp án:** IDS phát hiện/cảnh báo, IPS có thể chặn traffic.

## Câu 4
Site nào khôi phục nhanh nhất nhưng chi phí cao nhất?

**Đáp án:** Hot site.

## Câu 5
Data đang truyền qua mạng là trạng thái gì?

**Đáp án:** Data in transit.

## Câu 6
Giao thức nào dùng trong site-to-site VPN rất phổ biến?

**Đáp án:** IPsec.

## Câu 7
Trong IPsec, thành phần nào cung cấp encryption?

**Đáp án:** ESP.

## Câu 8
Một thiết bị chỉ copy traffic để phân tích, không block. Đây là inline hay TAP?

**Đáp án:** TAP / monitor mode.

## Câu 9
Một hệ thống công nghiệp không thể patch vì downtime nguy hiểm. Mitigation hợp lý là gì?

**Đáp án:** Segmentation, monitoring, compensating controls.

## Câu 10
Tokenization khác encryption thế nào?

**Đáp án:** Tokenization thay dữ liệu thật bằng token và cần token vault/map; encryption mã hóa bằng key và có thể giải mã bằng key.

---

# Ưu tiên ôn Module 3 trước ngày thi

## Mức bắt buộc

1. Shared responsibility matrix
2. Cloud models: IaaS/PaaS/SaaS
3. Network segmentation and security zones
4. IDS vs IPS
5. WAF vs NGFW vs UTM
6. VPN, TLS, IPsec, AH, ESP, IKE
7. 802.1X, EAP, RADIUS
8. Data states: at rest, in transit, in use
9. Masking vs tokenization vs encryption
10. Hot/warm/cold site and backup concepts

## Mức nên biết thêm

1. IaC risks and controls
2. Serverless risks
3. Container security
4. SD-WAN and SASE
5. IoT/ICS/SCADA/RTOS
6. Fail-open vs fail-closed
7. Load balancing vs clustering
8. Geographic dispersion and data sovereignty

---

# Một trang nhớ nhanh

```text
Module 3 = secure architecture design

Cloud:
Provider secures OF the cloud
Customer secures IN the cloud

Zones:
Internet → DMZ → Internal → Restricted
Guest should not access Internal
DB should not be directly exposed

Devices:
WAF = web app attacks
IDS = detect
IPS = block
Proxy = web control
Jump server = admin access
Load balancer = distribute traffic

VPN/IPsec:
ESP = encryption
AH = integrity/authentication
IKE = key exchange
Tunnel mode = whole packet
Transport mode = payload

Data:
At rest = stored → encryption
In transit = moving → TLS/VPN
In use = processing → access control/secure enclave

Recovery:
Hot = fastest/costliest
Cold = slowest/cheapest
Warm = middle
UPS = short power
Generator = longer power
```
