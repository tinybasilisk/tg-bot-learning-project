from telebot.types import Message
from loader import bot
from api import get_today_element, today_element_to_str, get_element_name
from database import User, log_command
from config_data import TODAY_DATE_FORMAT
import datetime


@bot.message_handler(commands=["today_element"])
def show_today_element(message: Message) -> None:
    """
    Handles the command to display information about the element of the day.
    Logs the command to the database associated with the User model.

    :param message: the user's command message
    :return:
    """
    user = User.get_or_none(User.user_id == message.from_user.id)
    if user is None:
        bot.reply_to(message, "You are not registered. Please use /start to continue.")
        return

    element = get_today_element()
    log_command(user=user, command="today_element", element_name=get_element_name(element))
    today_date = datetime.datetime.date(datetime.datetime.now()).strftime(TODAY_DATE_FORMAT)
    heading_text = "Today is {date}. The element of the day is:\n\n".format(date=today_date)
    element_text = today_element_to_str(element)
    bot.send_message(chat_id=message.chat.id, text=heading_text+element_text, parse_mode="HTML")
