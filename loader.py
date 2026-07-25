"""
This module initialises the bo and  loads all necessary modules.

"""

from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from config_data import BOT_TOKEN

storage = StateMemoryStorage()
bot = TeleBot(token=BOT_TOKEN, state_storage=storage)
