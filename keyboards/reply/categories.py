from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from api import ELEMENT_CATEGORIES


def gen_categories_markup():
    buttons = list()

    # create keyboard button objects
    for text_category in ELEMENT_CATEGORIES.values():
        button = KeyboardButton(text=text_category)
        buttons.append(button)

    # create keyboard object by adding in buttons
    keyboard = ReplyKeyboardMarkup()
    for button in buttons:
        keyboard.add(button)

    return keyboard
