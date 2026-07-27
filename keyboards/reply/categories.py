"""
This module handles creating a custom keyboard for choosing an element category.
"""


from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from api import ELEMENT_CATEGORIES


def gen_categories_markup() -> ReplyKeyboardMarkup:
    """
    Creates a reply keyboard with all element categories to process user response for the /guess_category command.

    :return: reply keyboard with all element categories
    """
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
