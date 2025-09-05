# -----------------------------
# TELEGRAM BOT - RAILWAY READY
# -----------------------------

import os
import telebot
import logging
from time import sleep

# ----- 1. Logging Setup -----
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ----- 2. Read BOT_TOKEN from Environment -----
TOKEN = os.environ.get("8208387299:AAHDkYSmeBQk7uccPhZqEj8r6TmLUnji4EY")
if not TOKEN:
    logger.error("BOT_TOKEN environment variable is missing! Exiting...")
    exit(1)

bot = telebot.TeleBot(TOKEN)

# ----- 3. Command Handlers -----
@bot.message_handler(commands=['start'])
def start_command(message):
    """Handles /start command"""
    bot.reply_to(message, f"Hello {message.from_user.first_name}! Bot is running on Railway 🚀")
    logger.info(f"/start used by {message.from_user.username or message.from_user.id}")

# ----- 4. Message Handler (Echo) -----
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    """Replies to any message with the same text"""
    bot.reply_to(message, f"You said: {message.text}")
    logger.info(f"Echoed message from {message.from_user.id}: {message.text}")

# ----- 5. Bot Runner with Auto-Restart -----
def run_bot():
    while True:
        try:
            logger.info("Bot is starting...")
            bot.infinity_polling(timeout=60)  # Checks messages continuously
        except Exception as e:
            logger.error(f"Bot crashed: {e}. Restarting in 5 seconds...")
            sleep(5)

# ----- 6. Start Bot -----
if __name__ == "__main__":
    run_bot()
