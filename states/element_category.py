"""
This module handles creating a state for awaiting user input on the element category in the /guess_category command.
"""

from telebot.handler_backends import State, StatesGroup


class ElementCategoryState(StatesGroup):
    category = State()
