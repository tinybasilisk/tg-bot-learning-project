"""
This module processes API server responses.

"""

from typing import Dict, Tuple
from .api_utils import ELEMENT_CATEGORIES
from functools import cache
from .api_requests import load_elements


def today_element_to_str(today_element_info: Dict[str, str | int]) -> str:
    """
    Produces a string representation of some of the information about the given element of the day.

    :param today_element_info: element information in json format
    :return: selected element information in str format
    """
    info_str = ("<b>{symbol}</b>\n{name}\n\nAtomic Number: {atomic_number}\nCategory: {category}\n"
                "Summary: {summary}\nDiscovery Year: {discovery_year}\n\nFun Fact: {fun_fact}").format(
        symbol=today_element_info["symbol"],
        name=today_element_info["name"],
        atomic_number=today_element_info["atomic_number"],
        category=ELEMENT_CATEGORIES[today_element_info["category"]],
        summary=today_element_info["summary"],
        discovery_year=today_element_info["discovery_year"],
        fun_fact=today_element_info["fun_fact"]
    )
    return info_str


@cache
def get_all_elements() -> Tuple[dict, ...]:
    """
    Loads all elements information when first run, caches the result and instantly returns it every time afterward.

    :return: a tuple with all elements data in json format
    """
    return tuple(load_elements())


def get_element_name(element: Dict[str, str | int]) -> str:
    """
    Returns the name of the element from the element json information.

    :param element: element information in json format
    :return: name of the element
    """
    return element["name"]


def get_element_category(element: Dict[str, str | int]) -> str:
    """
    Returns the category of the element in the format specified in api_utils.py.

    :param element: element information in json format
    :return: category of the element
    """
    return ELEMENT_CATEGORIES[element["category"]]
