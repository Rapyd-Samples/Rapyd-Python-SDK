"""
Creates a BaseService class.
Performs API calls,sets authentication tokens and handles http exceptions.

Class:
    BaseService
"""

import platform
from typing import List, Union
from enum import Enum
import re
from ..net.http_client import HTTPClient

from ..hooks.hook import CustomHook, Request, Response


class BaseService:
    """
    A class to represent a base serivce

    Attributes
    ----------
    _url_prefix : str
        The base URL

    Methods
    -------
    def set_base_url(url: str):
        Sets the base url
    """

    _url_prefix = "https://api.rapyd.net"

    _custom_hook = CustomHook()

    _http = HTTPClient(_custom_hook)

    def __init__(self) -> None:
        """
        Initialize client
        """

    def _pattern_matching(cls, value: str, pattern: str, variable_name: str):
        if re.match(r"{}".format(pattern), value):
            return value
        else:
            raise ValueError(f"Invalid value for {variable_name}: must match {pattern}")

    def _enum_matching(
        cls, value: Union[str, Enum], enum_values: List[str], variable_name: str
    ):
        str_value = value.value if isinstance(value, Enum) else value
        if str_value in enum_values:
            return value
        else:
            raise ValueError(
                f"Invalid value for {variable_name}: must match one of {enum_values}"
            )

    def set_base_url(self, url: str) -> None:
        """
        Sets the base URL

        Parameters:
        ----------
            url:
                The base URL
        """
        self._url_prefix = url

    def _add_required_headers(self, headers: dict):
        """
        Request authorization headers

        Parameters
        ----------
        headers: dict
            Headers dict to add auth headers to
        """
        headers["User-Agent"] = f"Rapydsdk/1.0.5 Python/{platform.python_version()}"

        return headers
