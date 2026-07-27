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
    ("guess_category", "guess the type of a random element"),
    ("history", "show previous commands")
)

# date format for loging command history
COMMAND_DATE_FORMAT = "%d-%m-%Y %H:%M"

# date format to display in /today_element command
TODAY_DATE_FORMAT = "%d-%m-%Y"
