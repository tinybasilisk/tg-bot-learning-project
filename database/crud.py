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
                block: str = None, criteria: str = None, ascending: bool = None) -> None:
    """
    Saves the command run by the user into the database the User models are associated with.

    :param user: the user who run the original command
    :param command: the command name string
    :param element_name: if applicable, the name of the element form the command response
    :param was_correct: if applicable, whether the user guessed the element category correctly
    :param block: if applicable, the block the element belongs to
    :param criteria: if applicable, the criteria the elements were sorted by
    :param ascending: if applicable, whether the sort order was ascending
    :return:
    """
    CommandHistory.create(
        user=user,
        command=command,
        element_name=element_name,
        was_correct=was_correct,
        # these are here for the remaining /show_top_five command
        block=block,
        criteria=criteria,
        ascending=ascending
    )
