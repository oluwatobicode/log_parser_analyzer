The alerts rules for the IPS were gotten from the GitHub (suricata-sample-data) , I scanned the sample logs and checked for patterns and critical logs the object in the logs that caught my attention was the alert , so I checked the alerts and saw some interesting stuffs 
- severity
- category 
- signature
then I created my log file like this 
- log_type
- field
- value 
- match_type
- level
- description 

the alerts rules would be passed into the parser and the log_type field would be used to detect what type of log_type the parser is checks the rules after that we will then pass it to the analzer