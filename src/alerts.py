import os
import asyncio
from dotenv import load_dotenv
from telegram import Bot
from parser import flagged_logs


load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("API_TOKEN")
phone_number = os.getenv("PHONE_NUMBER")
CHAT_ID = os.getenv("CHAT_ID")

# TELEGRAM BOTS FOR ALERTS
    # this creates the bot object
bot = Bot(token=TELEGRAM_BOT_TOKEN)

async def send_message(text,chat_id):
    async with bot:
        await bot.send_message(text=text, chat_id=chat_id)

async def run_bot(message,chat_id):
    text = '\n'.join(message)
    await send_message(text, chat_id)
    
    # TEXT MESSAGES
messages = [
    "Testing!",
    "Testing!",
    "Testing!"
    ]

if messages:
    asyncio.run(run_bot(messages, CHAT_ID))