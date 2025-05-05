from parser import flagged_logs

severity_map = {
    "low": 2,
    "medium": 4,
    "high": 5,
    "critical": 6
}

high_risk = []
low_risk = []

for log in flagged_logs:
    max_severity = 0

    for match in log["matches"]:
        level = match["level"].lower()
        severity = severity_map.get(level, 0)
        max_severity = max(max_severity, severity)

    if max_severity >= 5:
        high_risk.append(log)
    else:
        low_risk.append(log)

print(len(high_risk))

# looping through the high_risk 
with open("./reports/report_summary.txt", "w", encoding="utf-8") as f:
    for high_alert in high_risk:
        f.write(f"""
🚨 Log Analysis for HIGH RISK
Timestamp: {high_alert['timestamp']}
Source IP: {high_alert['src_ip']}
Destination IP: {high_alert['dest_ip']}
Risk Level: HIGH
Match Count: {len(high_alert['matches'])}
""")

    for low_alert in low_risk:
        f.write(f"""
⚠️ Log Analysis for LOW RISK
Timestamp: {low_alert['timestamp']}
Source IP: {low_alert['src_ip']}
Destination IP: {low_alert['dest_ip']}
Risk Level: LOW
Match Count: {len(low_alert['matches'])}
""")



