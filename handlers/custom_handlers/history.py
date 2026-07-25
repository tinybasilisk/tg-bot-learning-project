from telebot.types import Message
from loader import bot
from database import User, CommandHistory
from typing import List


@bot.message_handler(commands=["history"])
def show_history(message: Message) -> None:
    user = User.get_or_none(User.user_id == message.from_user.id)
    if user is None:
        bot.reply_to(message, "You are not registered. Please use /start to continue.")
        return

    commands: List[CommandHistory] = user.history.order_by(-CommandHistory.date_time).limit(10)

    result = []
    result.extend(map(str, reversed(commands)))
    if not result:
        bot.send_message(message.chat.id, "You don't have any command history yet.\nTry using some commands!")
        return
    bot.send_message(message.chat.id, "The last 10 commands in your command history:")
    text = "\n".join(result)
    bot.send_message(message.chat.id, f'<pre>{text}</pre>', parse_mode='HTML')
