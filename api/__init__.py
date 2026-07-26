"""
The api package handles all interaction with the API server.
Contains modules for handling API requests, processing the responses, and storing supporting utilities.

All data is provided by  PeriodicTableOfElements.org

"""

from .api_requests import get_today_element, load_elements
from .process_elements import today_element_to_str, get_all_elements, get_element_name, get_element_category
from .api_utils import ELEMENT_CATEGORIES
