# CloudGuardian: Serverless EC2 Snapshot Backup/Lifecycle Manager

A production-ready, cost-optimizing AWS Lambda automation suite engineered to manage Amazon EBS volume snapshots. This solution targets specific enterprise workloads using resource tagging metadata, enforces a strict 7-day backup retention compliance protocol, and compiles an automated runtime observability report.

Built using **Test-Driven Development (TDD)** principles, the entire application runtime is simulated and validated locally without provisioning live cloud infrastructure.

---

## 🚀 Key Architectural Features

* **Metadata-Driven Targeting:** Scans active EC2 topologies to isolate instances explicitly containing the compliance tag `Backup=True`.
* **Automated Lifecycle Auditing:** Identifies and purges stale automated snapshots older than 7 days, maintaining predictable cloud storage run-rates.
* **Dual-Reporting Engine:** Yields human-readable ASCII telemetry outputs directly to cloud execution logs and builds a self-contained HTML executive dashboard.
* **Local Simulation Grid:** Incorporates an isolated offline validation layer via `moto` to test destructive infrastructure routines securely with $0.00 cloud overhead.

---

## 🛠️ Technology Stack & Core Tools

* **Core Engine:** Python 3.x
* **AWS SDK Framework:** Boto3 (Amazon Web Services SDK for Python)
* **Mock Validation Grid:** Moto (Mock AWS Services Library)
* **Reporting Architecture:** Semantic HTML5 & CSS3
* **Shell Environment:** PowerShell Core

---

## 📂 Project Repository Blueprint

```text
serverless-ec2-backup-manager/
│
├── screenshots/
│   ├── cloudguardian-execution-flow.png  # Command-line execution telemetry
│   └── local-mock-architecture.png       # Generated HTML report artifact
│
├── lambda_function.py                     # Main AWS Lambda handler & business logic
├── test_local.py                          # Offline simulation setup & mock dataset
├── cloudguardian_report.html              # Dynamically generated runtime dashboard
└── README.md                              # Technical project documentation

⚙️ Local Infrastructure Simulation & Verification
1. Pre-requisites & Local Workspace Isolation
Install the required application engineering packages within your local interpreter using PowerShell:

PowerShell
pip install boto3 moto
2. Executing the Local Simulation Suite
The application includes a specialized mocking harness (test_local.py). This script maps out a simulated AWS region in system memory, provisions a target database server, drops an untagged sandbox server, injects an expired volume snapshot, and triggers the core handler:

PowerShell
python test_local.py
📊 Operational Telemetry & Proof of Performance
Command-Line Execution Output
Upon execution, the script evaluates the active landscape, skips non-compliant machines, and builds a comprehensive processing record:

Automated Executive HTML Dashboard
The solution constructs an output dashboard asset locally on every single successful execution lifecycle, detailing compliance changes and actions taken:

🧠 Technical Highlights for Technical Recruiters
Designed for Cost Efficiency: Solves the common corporate problem of "zombie storage" by automating cleanup rules, instantly reducing AWS data retention bills.

Decoupled Local Testing: Eliminates developer dependency on active AWS sandboxes by constructing deterministic mock states, allowing testing cycles to move faster.

Least-Privilege Security Design: Engineered explicitly to conform to standard AWS IAM role structures, requiring only minimal read/write granular permissions (ec2:CreateSnapshot, ec2:DescribeSnapshots, ec2:DeleteSnapshot).