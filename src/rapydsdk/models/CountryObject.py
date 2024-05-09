from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class CountryObject(BaseModel):
    def __init__(
        self,
        currency_code: str = None,
        currency_name: str = None,
        currency_sign: str = None,
        id: float = None,
        iso_alpha2: str = None,
        iso_alpha3: str = None,
        name: str = None,
        phone_code: str = None,
    ):
        self.currency_code = currency_code
        self.currency_name = currency_name
        self.currency_sign = currency_sign
        self.id = id
        self.iso_alpha2 = iso_alpha2
        self.iso_alpha3 = iso_alpha3
        self.name = name
        self.phone_code = phone_code
