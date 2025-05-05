import os
import sys
import asyncio
from dotenv import load_dotenv


"""
Log Analyzer Main Script
------------------------
This script ties together all components of the log analyzer system:
1. Parser - Processes log files and matches them against rules
2. Analyzer - Categorizes logs by severity
3. Alerts - Sends notifications via Telegram

"""

# this Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from src.parser import flagged_logs
from src.analyzer import high_risk, low_risk
from src.alerts import run_alerts

# this makes sure the environment variables are loaded first
load_dotenv()


print("Starting log analysis process...")

# Step 1: we Parse the logs and apply rules (this makes that flagged_logs)
print("Parsing logs and matching rules...")
print(f"Parsing complete. Found {len(flagged_logs)} flagged logs.")

# Step 2: Analyze logs and categorize by risk level
print("Analyzing and categorizing logs...")
print(f"Analysis complete. Found {len(high_risk)} high risk and {len(low_risk)} low risk issues.")

# Step 3: Send alerts for high risk issues
print("Sending alerts...")
asyncio.run(run_alerts())

print("Log analysis process completed!")