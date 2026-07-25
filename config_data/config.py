"""
This module sets up the main bot parameters used for configuring the bot.

"""

import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Environment variables not loaded as there is no .env file")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DB_PATH = "database.db"

DEFAULT_COMMANDS = (
    ("start", "start the bot"),
    ("help", "show all commands"),
    ("today_element", "show the element of the day"),
    ("guess_category", "guess the type of a random element")
)
