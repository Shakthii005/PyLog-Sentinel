import re
import logging
import json
import csv
from collections import defaultdict

with open("network_logs.txt", "r") as f:
    logs = f.readlines()

parsed_logs = []
for line in logs:
    match = re.match(r"(\w+\s+\d+\s+\d+:\d+:\d+) (\w+) %\S+-(\d+)-\S+: (.*)", line)
    if match:
        timestamp, device, severity, message = match.groups()
        parsed_logs.append({
            "timestamp": timestamp,
            "device": device,
            "severity": severity,
            "message": message
        })

failed_logins = defaultdict(int)   
denied_traffic = defaultdict(int)  


logging.basicConfig(
    filename="security_alerts.log",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

for entry in parsed_logs:
    msg = entry["message"]

    login_fail = re.search(r"Login failed.*from (\d+\.\d+\.\d+\.\d+)", msg)
    if login_fail:
        ip = login_fail.group(1)
        failed_logins[ip] += 1
        if failed_logins[ip] >= 3:
            alert_msg = f"Possible brute-force attack from {ip} - {failed_logins[ip]} failed logins"
            print(alert_msg)
            logging.warning(alert_msg)

    login_success = re.search(r"Login successful.*from (\d+\.\d+\.\d+\.\d+)", msg)
    if login_success:
        ip = login_success.group(1)
        if failed_logins[ip] >= 3:
            alert_msg = f" Possible brute-force SUCCESS from {ip} - {failed_logins[ip]} failures followed by success"
            print(alert_msg)
            logging.warning(alert_msg)
        failed_logins[ip] = 0 

    
    deny_match = re.search(r"denied \w+ (\d+\.\d+\.\d+\.\d+)\(\d+\)", msg)
    if deny_match:
        ip = deny_match.group(1)
        denied_traffic[ip] += 1
        if denied_traffic[ip] >= 3:
            alert_msg = f" Possible port scan from {ip} - {denied_traffic[ip]} denies"
            print(alert_msg)
            logging.warning(alert_msg)

with open("parsed_logs.json", "w") as f:
    json.dump(parsed_logs, f, indent=4)

with open("parsed_logs.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=parsed_logs[0].keys())
    writer.writeheader()
    writer.writerows(parsed_logs)

print("Log analysis complete. Alerts saved in security_alerts.log, structured logs in JSON/CSV.")
