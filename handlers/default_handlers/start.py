from loader import bot
from telebot.types import Message
from database.models import User
from peewee import IntegrityError
from config_data.config import DEFAULT_COMMANDS

@bot.message_handler(commands=["start"])
def bot_help(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    try:
        User.create(
            user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        bot.reply_to(message, "Hello, {name}!".format(name=first_name))
    except IntegrityError:
        bot.reply_to(message, "It's good to see you again, {name}!".format(name=first_name))
