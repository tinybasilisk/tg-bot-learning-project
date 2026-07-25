from loader import bot
from telebot.types import Message, ReplyKeyboardRemove
from config_data import DEFAULT_COMMANDS


@bot.message_handler(commands=["help"])
def bot_help(message: Message) -> None:
    """
    Explains the bot's functionality by listing available commands. Removes any applied states or keyboards.

    :param message: the user's message
    :return:
    """
    intro_text = "Here is what I can do:\n"
    commands_text = "\n".join([f"/{command} - {desc}" for command, desc in DEFAULT_COMMANDS])
    bot.send_message(chat_id=message.chat.id, text=intro_text+commands_text, reply_markup=ReplyKeyboardRemove())
    bot.delete_state(user_id=message.from_user.id, chat_id=message.chat.id)
