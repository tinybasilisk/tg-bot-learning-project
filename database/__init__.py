"""
The database package handles all interation with databases.
Contains modules for creating and queering databases and working with data models.

"""

from .crud import create_models, log_command
from .models import db, BaseModel, User, CommandHistory
