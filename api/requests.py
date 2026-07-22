"""
This module handles direct API requests to https://api.periodictableofelements.org.

"""

import requests
from typing import Dict


def get_today_element() -> Dict[str, str | int]:
    """
    Gets information on the element of the day.

    :return: element data in json format
    """
    today_element_info = requests.get("https://api.periodictableofelements.org/elements/element-of-the-day/").json()
    return today_element_info



