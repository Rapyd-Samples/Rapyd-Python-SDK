from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class ScreenColorDepth(Enum):
    """An enumeration representing different categories.

    :cvar _1: 1
    :vartype _1: int
    :cvar _4: 4
    :vartype _4: int
    :cvar _8: 8
    :vartype _8: int
    :cvar _15: 15
    :vartype _15: int
    :cvar _16: 16
    :vartype _16: int
    :cvar _24: 24
    :vartype _24: int
    :cvar _32: 32
    :vartype _32: int
    :cvar _48: 48
    :vartype _48: int
    """

    _1 = 1
    _4 = 4
    _8 = 8
    _15 = 15
    _16 = 16
    _24 = 24
    _32 = 32
    _48 = 48

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ScreenColorDepth._member_map_.values()))


@JsonMap({})
class ClientDetailsObject(BaseModel):
    """Describes the fields in the client_details object in REST messages for payments. The client_details object describes the browser that the customer is using. The client collects this information and sends it as part of the Create Payment request. This information is used for processing the 3DS version 2 authentication of the customer. Note that Client Details information is not returned in the API response and it does not appear in any webhooks.

    :param ip_address: IP address of the customer., defaults to None
    :type ip_address: str, optional
    :param java_enabled: Indicates whether the browser is enabled for Java., defaults to None
    :type java_enabled: bool, optional
    :param java_script_enabled: Indicates whether the browser is enabled for JavaScript., defaults to None
    :type java_script_enabled: bool, optional
    :param language: The language the browser is configured for, as defined in IETF BCP 47., defaults to None
    :type language: str, optional
    :param screen_color_depth: Indicates the screen color depth of the customer's browser, in bits., defaults to None
    :type screen_color_depth: ScreenColorDepth, optional
    :param screen_height: Height of the customer's screen, in pixels. 1-6 digits., defaults to None
    :type screen_height: int, optional
    :param screen_width: Width of the customer's screen, in pixels. 1-6 digits., defaults to None
    :type screen_width: int, optional
    :param time_zone_offset: Difference in minutes between UTC and the customer's time zone. Positive or negative integer., defaults to None
    :type time_zone_offset: int, optional
    """

    def __init__(
        self,
        ip_address: str = None,
        java_enabled: bool = None,
        java_script_enabled: bool = None,
        language: str = None,
        screen_color_depth: ScreenColorDepth = None,
        screen_height: int = None,
        screen_width: int = None,
        time_zone_offset: int = None,
    ):
        """Describes the fields in the client_details object in REST messages for payments. The client_details object describes the browser that the customer is using. The client collects this information and sends it as part of the Create Payment request. This information is used for processing the 3DS version 2 authentication of the customer. Note that Client Details information is not returned in the API response and it does not appear in any webhooks.

        :param ip_address: IP address of the customer., defaults to None
        :type ip_address: str, optional
        :param java_enabled: Indicates whether the browser is enabled for Java., defaults to None
        :type java_enabled: bool, optional
        :param java_script_enabled: Indicates whether the browser is enabled for JavaScript., defaults to None
        :type java_script_enabled: bool, optional
        :param language: The language the browser is configured for, as defined in IETF BCP 47., defaults to None
        :type language: str, optional
        :param screen_color_depth: Indicates the screen color depth of the customer's browser, in bits., defaults to None
        :type screen_color_depth: ScreenColorDepth, optional
        :param screen_height: Height of the customer's screen, in pixels. 1-6 digits., defaults to None
        :type screen_height: int, optional
        :param screen_width: Width of the customer's screen, in pixels. 1-6 digits., defaults to None
        :type screen_width: int, optional
        :param time_zone_offset: Difference in minutes between UTC and the customer's time zone. Positive or negative integer., defaults to None
        :type time_zone_offset: int, optional
        """
        self.ip_address = self._define_str("ip_address", ip_address, nullable=True)
        self.java_enabled = java_enabled
        self.java_script_enabled = java_script_enabled
        self.language = self._define_str("language", language, nullable=True)
        self.screen_color_depth = (
            self._enum_matching(
                screen_color_depth, ScreenColorDepth.list(), "screen_color_depth"
            )
            if screen_color_depth
            else None
        )
        self.screen_height = self._define_number(
            "screen_height", screen_height, nullable=True
        )
        self.screen_width = self._define_number(
            "screen_width", screen_width, nullable=True
        )
        self.time_zone_offset = self._define_number(
            "time_zone_offset", time_zone_offset, nullable=True
        )
