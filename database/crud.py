"""
This module handles creating and queering databases.

"""

from .models import BaseModel, db, User, CommandHistory


def create_models() -> None:
    """
    Initialises the common database to store information on all users.
    :return:

    """
    db.create_tables(BaseModel.__subclasses__())


def log_command(user: User, command: str, element_name: str = None, was_correct: bool = None,
                block: str = None, criteria: str = None, ascending: bool= None):
    CommandHistory.create(
        user=user,
        command=command,
        element_name=element_name,
        was_correct=was_correct,
        block=block,
        criteria=criteria,
        ascending=ascending
    )
