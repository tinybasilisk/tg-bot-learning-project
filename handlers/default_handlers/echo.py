from telebot.types import Message, ReplyKeyboardRemove
from loader import bot


@bot.message_handler(state=None)
def bot_echo(message: Message) -> None:
    """
    Handles all messages with no state or command filters. Removes any applied states or keyboards.

    :param message: the user's message
    """
    bot.reply_to(
        message=message,
        text="I cannot understand this command.\nTo see available commands, use /help.",
        reply_markup=ReplyKeyboardRemove()
    )
    bot.delete_state(user_id=message.from_user.id, chat_id=message.chat.id)
