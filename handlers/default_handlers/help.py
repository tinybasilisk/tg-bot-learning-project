from loader import bot
from telebot.types import Message, ReplyKeyboardRemove
from config_data import DEFAULT_COMMANDS
from database import User, log_command


@bot.message_handler(commands=["help"])
def bot_help(message: Message) -> None:
    """
    Explains the bot's functionality by listing available commands. Removes any applied states or keyboards.

    :param message: the user's message
    :return:
    """
    user = User.get_or_none(User.user_id == message.from_user.id)
    if user is None:
        bot.reply_to(message, "You are not registered. Please use /start to continue.")
        return

    intro_text = "Here is what I can do:\n"
    commands_text = "\n".join([f"/{command} - {desc}" for command, desc in DEFAULT_COMMANDS])
    bot.send_message(chat_id=message.chat.id, text=intro_text+commands_text, reply_markup=ReplyKeyboardRemove())
    bot.delete_state(user_id=message.from_user.id, chat_id=message.chat.id)
    log_command(user=user, command="help")