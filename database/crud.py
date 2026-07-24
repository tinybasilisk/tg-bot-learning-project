"""
This module handles creating and queering databases.

"""

from database.models import BaseModel, db


def create_models() -> None:
    """
    Initialises the common database to store information on all users.
    :return:

    """
    db.create_tables(BaseModel.__subclasses__())
