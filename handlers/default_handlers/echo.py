from telebot.types import Message
from loader import bot


@bot.message_handler(state=None)
def bot_echo(message: Message) -> None:
    """
    Handles all messages with no state filters.

    :param message: the user's message
    """
    bot.reply_to(
        message, "I cannot understand this command.\nTo see available commands, use /help."
    )
