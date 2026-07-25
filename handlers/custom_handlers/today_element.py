from telebot.types import Message
from loader import bot
from api import get_today_element, today_element_to_str


@bot.message_handler(commands=["today_element"])
def show_today_element(message: Message) -> None:
    """
    Handles the command to display information about the element of the day.

    :param message: the user's message
    :return:
    """
    element = get_today_element()
    output_text = today_element_to_str(element)
    bot.send_message(chat_id=message.chat.id, text=output_text, parse_mode="HTML")
