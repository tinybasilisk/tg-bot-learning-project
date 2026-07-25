from telebot.types import Message, ReplyKeyboardRemove
from loader import bot
from api import get_all_elements, ELEMENT_CATEGORIES, get_element_name, get_element_category
from keyboards import gen_categories_markup
from states import ElementCategoryState
import random


@bot.message_handler(commands=["guess_category"])
def bot_guess_category(message: Message):
    all_elements_tuple = get_all_elements()
    element = random.choice(all_elements_tuple)
    question = "The element is called <b>{element_name}</b>.\n\nWhat type of element is it?".format(
        element_name=get_element_name(element=element)
    )
    bot.send_message(
        chat_id=message.chat.id, text=question, reply_markup=gen_categories_markup(), parse_mode="HTML"
    )
    with bot.retrieve_data(user_id=message.from_user.id, chat_id=message.chat.id) as data:
        data["element"] = element
        bot.set_state(user_id=message.from_user.id, state=ElementCategoryState.category, chat_id=message.chat.id)


@bot.message_handler(state=ElementCategoryState.category)
def process_element_category(message: Message):
    user_answer = message.text
    if user_answer not in ELEMENT_CATEGORIES.values():
        # handles user not using the keyboard
        bot.send_message(chat_id=message.chat.id, text="Unknown category! Please use the keyboard to answer.")
    else:
        with bot.retrieve_data(user_id=message.from_user.id, chat_id=message.chat.id) as data:
            element = data["element"]
            if user_answer == get_element_category(element):
                feedback = "That's correct!"
            else:
                feedback = "That's wrong."
            bot.delete_state(user_id=message.from_user.id, chat_id=message.chat.id)
            bot.send_message(chat_id=message.chat.id, text=feedback, reply_markup=ReplyKeyboardRemove())
