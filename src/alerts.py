import os
import asyncio
from dotenv import load_dotenv
from telegram import Bot
from analyzer import high_risk, low_risk

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("API_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Initialize the bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)

async def send_message(text, chat_id):
    #Sends a single message through the Telegram bot
    async with bot:
        await bot.send_message(text=text, chat_id=chat_id)

async def send_alert_batch(alerts, risk_level, chat_id):
    # Send a batch of alerts with specified risk level
    if not alerts:
        return
        
    # Send a summary message of the logs first
    summary = f"🚨 {len(alerts)} {risk_level.upper()} RISK ALERTS DETECTED 🚨"
    await send_message(summary, chat_id)
    
    # Sends a detailed alerts (i limited to 5 to avoid spam)
    for i, alert in enumerate(alerts[:5]):
        message = f"""
{i+1}. {risk_level.upper()} RISK ALERT:
Timestamp: {alert['timestamp']}
Source IP: {alert['src_ip']}
Destination IP: {alert['dest_ip']}
Match Count: {len(alert['matches'])}

Top Match: {alert['matches'][0]['level']} - {alert['matches'][0]['description']}
        """
        await send_message(message, chat_id)
    
    # If there are more alerts than we showed
    if len(alerts) > 5:
        await send_message(f"... and {len(alerts) - 5} more {risk_level} risk alerts. See full report for details.", chat_id)

async def run_alerts():
    """Main function to send all alerts"""
    if high_risk:
        await send_alert_batch(high_risk, "high", CHAT_ID)
    
    if low_risk:
        await send_alert_batch(low_risk, "low", CHAT_ID)
    
    # Notify about the complete analysis
    total_alerts = len(high_risk) + len(low_risk)
    if total_alerts > 0:
        await send_message(f"✅ Log analysis complete. Found {len(high_risk)} high risk and {len(low_risk)} low risk alerts.", CHAT_ID)
    else:
        await send_message("✅ Log analysis complete. No risk alerts detected.", CHAT_ID)

# Execute the alerts if this script is run directly
if __name__ == "__main__":
    asyncio.run(run_alerts())