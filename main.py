from database import create_models
from loader import bot
import handlers # noqa: 401
from utils import set_default_commands
from telebot.custom_filters import StateFilter


if __name__ == "__main__":
    create_models()
    set_default_commands(bot)
    bot.add_custom_filter(StateFilter(bot))
    bot.infinity_polling()
