from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class MerchantCustomerSupport(BaseModel):
    def __init__(
        self,
        email: str = None,
        url: str = None,
        phone_number: str = None,
        merchant_logo: str = None,
    ):
        self.email = email
        self.url = url
        self.phone_number = phone_number
        self.merchant_logo = merchant_logo
