from telebot.handler_backends import State, StatesGroup


class ElementCategoryState(StatesGroup):
    category = State()
