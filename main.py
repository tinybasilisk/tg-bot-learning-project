from database.crud import create_models
from loader import bot
import handlers # noqa: 401
from utils.set_bot_commands import set_default_commands


if __name__ == "__main__":
    create_models()
    set_default_commands(bot)
    bot.infinity_polling()

