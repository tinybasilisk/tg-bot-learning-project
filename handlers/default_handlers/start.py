from loader import bot
from telebot.types import Message, ReplyKeyboardRemove
from database import User
from peewee import IntegrityError
from .help import bot_help


@bot.message_handler(commands=["start"])
def bot_start(message: Message) -> None:
    """
    Greets the user based on prior chat history
    and launches the /help command to introduce available commands.

    :param message: the user's message
    :return:
    """
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    try:
        User.create(
            user_id=user_id,
            username=username,
            first_name=first_name,
        )
    except IntegrityError:
        greeting_text = "It's good to see you again, {name}!".format(name=first_name)
    else:
        greeting_text = "Hello, {name}!".format(name=first_name)
    finally:
        intro_text = "\nI can tell you a bit about the elements in the Periodic Table."
        bot.send_message(chat_id=message.chat.id, text=greeting_text+intro_text)
        bot_help(message)
