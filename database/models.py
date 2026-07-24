"""
This module handles working with data models.

"""

from peewee import SqliteDatabase, Model, CharField, IntegerField
from config_data.config import DB_PATH

db = SqliteDatabase(DB_PATH)


class BaseModel(Model):
    """
    Abstract superclass used to connect all future models to the same database.

    """
    class Meta:
        database = db


class User(BaseModel):
    """
    The class models a user by tracking their Telegram user id, username,
    first name from profile, and last name from profile.

    """
    user_id = IntegerField(primary_key=True)
    username = CharField()
    first_name = CharField()
    last_name = CharField(null=True)
