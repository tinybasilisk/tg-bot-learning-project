"""
This module processes API server responses.

"""

from typing import Dict
from api.api_utils import ELEMENT_CATEGORIES


def today_element_to_str(today_element_info: Dict[str, str | int]) -> str:
    """
    Produces a string representation of some of the information about the given element of the day.

    :param today_element_info: element information in json format
    :return: selected element information in str format
    """
    heading = f'<b>{today_element_info["symbol"]}</b>\n'
    body = ("{name}\n\nAtomic Number: {atomic_number}\nCategory: {category}\n"
            "Summary: {summary}\nDiscovery Year: {discovery_year}\n\nFun Fact: {fun_fact}").format(
        name=today_element_info["name"],
        atomic_number=today_element_info["atomic_number"],
        category=ELEMENT_CATEGORIES[today_element_info["category"]],
        summary=today_element_info["summary"],
        discovery_year=today_element_info["discovery_year"],
        fun_fact=today_element_info["fun_fact"]
    )
    return heading + body
