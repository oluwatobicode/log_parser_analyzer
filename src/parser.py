import json

flagged_logs = []

# reading the rules files
with open("./rules/ids_rules.json", "r", encoding="utf-8") as file:
    ids_sample_rules = json.load(file)



# reading the json file
with open('./logs/alerts-only.json', "r", encoding="utf-8") as file:
    ids_sample_logs = json.load(file)


# function to match the rules
def match_rules(logs_entry, rules):
    field_part = rules["field"].split(".")
    ["alert", "signature"]
    value = logs_entry

    for part in field_part:
        value = value.get(part) if isinstance(value, dict) else None
        
    if value is None:
        return False
    
    match_type = rules.get("match_type")
    rule_value = rules["value"]

    if match_type == "contains":
        # print(rule_value.lower())
        # print(str(value.lower()))
        return rule_value.lower() in str(value).lower()
    elif match_type == "equals":
        return str(value).lower() == str(rule_value).lower()
    elif match_type == "gte":
        return float(value) >= float(rule_value)

    return False


# looping through the sample logs and comparing them with with ids_rules
for ids_logs in ids_sample_logs:
    for ids_rules in ids_sample_rules:
        if ids_rules["log_type"] != "ids":
            continue
        if match_rules(ids_logs, ids_rules):
            logs_key = (
                ids_logs["timestamp"],
                ids_logs["src_ip"],
                ids_logs["dest_ip"]
            )

            existing_log = next(
               (log for log in flagged_logs
                if log["timestamp"] == logs_key[0] and
                log["src_ip"] == logs_key[1] and
                log["dest_ip"] == logs_key[2]),
                None
            )

            if existing_log:
                existing_log["matches"].append({
                    "level": ids_rules["level"],
                    "description": ids_rules["description"]
                })
            else:
                flagged_logs.append({
                "timestamp":ids_logs["timestamp"],
                "dest_ip":ids_logs["dest_ip"],
                "src_ip":ids_logs["src_ip"],
                "matches":[
                    {
                    "level":ids_rules["level"],
                    "description":ids_rules["description"]
                    }
                ]
            })

print(flagged_logs)
print(f"Processed {len(ids_sample_logs)}, flagged:{len(flagged_logs)} logs")



# kindly ignore my thought process 😂

# encounterd an issue of getting processed:44 flags,flagged:93
# this was because a log matched multiple rules and was being pushed more
#  than once into my flagged_logs = [] array
#  currently when we loop through all our ids logs
#  for each log we get loop with all our rules 
#  if the logs matches more than one rule, it is added to 
#  the flagged_logs multiple times - one for each match


# HOW to FIX IT 
#  1. i checked the array for duplicate logs
#  2. if there is i appended the new match (level,description) to what rules it matches
#  3. if no i created a new log entry with matches initalized


# basically i changed the output of the log to that so instaed of multiple 
# logs with different matches one match per log is done

# {
#   "timestamp": "...",
#   "src_ip": "...",
#   "dest_ip": "...",
#   "matches": [
#     {
#       "level": "critical",
#       "description": "SSH Scan Detected"
#     },
#     {
#       "level": "medium",
#       "description": "Suspicious access to port 3306"
#     }
#   ]
# }
