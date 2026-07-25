"""
This module handles working with data models.

"""
from fontTools.unicodedata import block
from peewee import SqliteDatabase, Model, CharField, IntegerField, ForeignKeyField, BooleanField, \
    DateTimeField
from config_data import DB_PATH, DATE_FORMAT
import datetime

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


class CommandHistory(BaseModel):
    user = ForeignKeyField(User, backref="history")
    date_time = DateTimeField(default=datetime.datetime.now)
    command = CharField()
    # for guess_category and today_element commands
    element_name = CharField(null=True)
    # for guess_category command
    was_correct = BooleanField(null=True)
    # for show_top_five command
    block = CharField(null=True)
    criteria = CharField(null=True)
    ascending = BooleanField(null=True)

    def __str__(self):
        time_str = self.date_time.strftime(DATE_FORMAT)
        line = f"{time_str} — /{self.command:<15}"
        if self.element_name is not None:
            line += f" {self.element_name:<15}"
        if self.was_correct is not None:
            line += " guessed correctly" if self.was_correct else " guessed wrong"
        # if None not in (self.block, self.criteria, self.ascending):
        #     line += f"block: {self.block} sorted {self.criteria:<20} ascending: {self.ascending}"
        return line
