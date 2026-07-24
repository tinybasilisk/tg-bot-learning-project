from telebot import TeleBot
from telebot.types import BotCommand
from config_data.config import DEFAULT_COMMANDS


def set_default_commands(bot: TeleBot) -> None:
    """
    Sets up commands used to interact with the bot.
    :param bot: the configured bot
    :return:
    """
    bot.set_my_commands([BotCommand(*i) for i in DEFAULT_COMMANDS])
