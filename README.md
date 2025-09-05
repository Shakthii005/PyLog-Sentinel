# PyLog-Sentinel 🔎🛡️  
A lightweight, open-source log analysis and threat detection tool built with Python
###
BLOG FOR THIS PROJECT : https://medium.com/@rukhuraj1/building-pylog-sentinel-my-mini-soc-project-in-python-f225495b9b56
## 🚀 Overview
PyLog-Sentinel is a beginner-friendly, open-source **Mini-SOC log analyzer** designed for students and aspiring **Network Security Engineers**.  
It ingests raw network device logs (Cisco-style), parses them into structured data, applies detection rules, and generates security alerts for:  

- 🚨 Brute-force login attempts  
- 🚨 Brute-force success (after multiple failures)  
- ⚠️ Port scans / repeated denied traffic  

This project was built as part of my **Cybersecurity + Network Security learning journey**, and is fully **open-source** so others can build upon it.  

---

## ✨ Features

- Parses raw text logs into **structured JSON and CSV**  
- Detects brute-force login attempts  
- Detects brute-force success (post login failures)  
- Detects port scans via repeated ACL denies  
- Stores alerts in a dedicated **security log file**  
- CLI-ready script for easy execution  

---

## 📂 File Structure

│── analyzer.py # Main log analyzer script
│── network_logs.txt # Sample log file for testing
│── security_alerts.log # Generated alerts file
│── parsed_logs.json # Exported structured logs (JSON)
│── parsed_logs.csv # Exported structured logs (CSV)
│── README.md # Documentation

---

## 🛠️ Usage
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/PyLog-Sentinel.git
   cd PyLog-Sentinel

2. Run analyzer with sample logs:
   python analyzer.py

3. View results:
security_alerts.log → Alerts with timestamps
parsed_logs.json → Structured logs (JSON)
parsed_logs.csv → Structured logs (CSV)

-------------------

## Why This Project?

As an aspiring Network Security Engineer, I built PyLog-Sentinel to:

Strengthen my Python skills in logging, regex, and parsing

Learn how security teams (SOCs) handle log analysis

Demonstrate practical skills to internship recruiters & SFS program reviewers

This project is intentionally lightweight, but it mirrors real SOC workflows:
Logs → Parse → Detect → Alert → Export

-----------------------------
## Open Source

PyLog-Sentinel is released as open-source (MIT License).
Anyone can fork, extend, or contribute detection rules.
Future plans include adding support for firewall logs, IDS alerts, and SIEM integration.

---------------------
## Author

Shakthivel Rajesh

🎓 B.Tech CSE (Cybersecurity Specialization), SRM University

🛡️ CompTIA Network+ Certified | Google Cybersecurity Certificate

🌎 Aspiring Network Security Engineer 

📧 svelr005@gmail.com

https://www.linkedin.com/in/svelr005/
