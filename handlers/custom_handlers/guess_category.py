from telebot.types import Message, ReplyKeyboardRemove
from loader import bot
from api import get_all_elements, ELEMENT_CATEGORIES, get_element_name, get_element_category
from keyboards import gen_categories_markup
from states import ElementCategoryState
from database import User, log_command
import random


@bot.message_handler(commands=["guess_category"])
def bot_guess_category(message: Message) -> None:
    """
    Handles the command to have the user try to guess the category of a random element. Uses a custom keyboard.
    Logs the command to the database associated with the User model.

    :param message: the user's command message
    :return:
    """

    user = User.get_or_none(User.user_id == message.from_user.id)
    if user is None:
        bot.reply_to(message, "You are not registered. Please use /start to continue.")
        return

    all_elements_tuple = get_all_elements()
    element = random.choice(all_elements_tuple)
    question = "Try to guess the category of a random element.\nWhat type of element is <b>{element_name}</b>?".format(
        element_name=get_element_name(element=element)
    )
    bot.send_message(
        chat_id=message.chat.id, text=question, reply_markup=gen_categories_markup(), parse_mode="HTML"
    )
    with bot.retrieve_data(user_id=user.user_id, chat_id=message.chat.id) as data:
        data["element"] = element
        bot.set_state(user_id=user.user_id, state=ElementCategoryState.category, chat_id=message.chat.id)


@bot.message_handler(state=ElementCategoryState.category)
def process_element_category(message: Message) -> None:
    """
    Processes the user input through a custom keyboard, handles any other text messages.
    Logs the command to the database associated with the User model.

    :param message: the user's message, text or custom keyboard input
    :return:
    """
    user_answer = message.text
    if user_answer not in ELEMENT_CATEGORIES.values():
        # handles user not using the keyboard
        bot.send_message(chat_id=message.chat.id, text="Unknown category! Please use the keyboard to answer.")
    else:
        user = User.get(User.user_id == message.from_user.id)
        with bot.retrieve_data(user_id=user.user_id, chat_id=message.chat.id) as data:
            element = data["element"]
            if user_answer == get_element_category(element):
                feedback = "That's correct! Good guess."
                log_command(user=user, command="guess_category",
                            element_name=get_element_name(element), was_correct=True)
            else:
                feedback = "That's wrong. Maybe try another time."
                log_command(user=user, command="guess_category",
                            element_name=get_element_name(element), was_correct=False)
            bot.delete_state(user_id=user.user_id, chat_id=message.chat.id)
            bot.send_message(chat_id=message.chat.id, text=feedback, reply_markup=ReplyKeyboardRemove())
