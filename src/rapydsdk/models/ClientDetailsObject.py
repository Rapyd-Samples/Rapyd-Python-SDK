from enum import Enum
from .utils.JsonMap import JsonMap
from .base import BaseModel


class ScreenColorDepth(Enum):
    V1 = 1
    V4 = 4
    V8 = 8
    V15 = 15
    V16 = 16
    V24 = 24
    V32 = 32
    V48 = 48

    def list():
        return list(map(lambda x: x.value, ScreenColorDepth._member_map_.values()))


@JsonMap({})
class ClientDetailsObject(BaseModel):
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
        self.ip_address = ip_address
        self.java_enabled = java_enabled
        self.java_script_enabled = java_script_enabled
        self.language = language
        self.screen_color_depth = (
            self._enum_matching(
                screen_color_depth, ScreenColorDepth.list(), "screen_color_depth"
            )
            if screen_color_depth
            else None
        )
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.time_zone_offset = time_zone_offset
