from parser import flagged_logs

# this dictionary assigns a numeric value to each severity level
# and it is used for comparing the severity level easily using
# numbers

severity_map = {
    "low": 2,
    "medium": 4,
    "high": 5,
    "critical": 6
}

# an empty array for the high flagged logs risk(critical ones)
high_risk = []
# an empty array for the low flagged logs risk (not so critical ones)
low_risk = []

# looping through all the flagged logs
for log in flagged_logs:
    max_severity = 0 # reset max severity for this log

    for match in log["matches"]:
        level = match["level"].lower() #converted to lower-case for easy read
        severity = severity_map.get(level, 0) # converts the level to numbers
        max_severity = max(max_severity, severity) # this help me tracking the severity in this log

    # After checking all matches this decide if the log is high or low risk
    if max_severity >= 5:
        high_risk.append(log)
    else:
        low_risk.append(log)

# print(len(high_risk))

# looping through the high_risk and low risk and writing it to a file
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



