from database.models import create_models
from loader import bot
import handlers # noqa: 401
from utils.set_bot_commands import set_default_commands
from api.requests import load_all_elements_as_json

if __name__ == "__main__":
    create_models()
    set_default_commands(bot)
    # load_all_elements_as_json()
    bot.infinity_polling()
