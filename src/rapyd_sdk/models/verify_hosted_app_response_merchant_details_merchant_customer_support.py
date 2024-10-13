from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class VerifyHostedAppResponseMerchantDetailsMerchantCustomerSupport(BaseModel):
    """VerifyHostedAppResponseMerchantDetailsMerchantCustomerSupport

    :param email: email, defaults to None
    :type email: str, optional
    :param url: url, defaults to None
    :type url: str, optional
    :param phone_number: phone_number, defaults to None
    :type phone_number: str, optional
    """

    def __init__(self, email: str = None, url: str = None, phone_number: str = None):
        """VerifyHostedAppResponseMerchantDetailsMerchantCustomerSupport

        :param email: email, defaults to None
        :type email: str, optional
        :param url: url, defaults to None
        :type url: str, optional
        :param phone_number: phone_number, defaults to None
        :type phone_number: str, optional
        """
        self.email = self._define_str("email", email, nullable=True)
        self.url = self._define_str("url", url, nullable=True)
        self.phone_number = self._define_str(
            "phone_number", phone_number, nullable=True
        )
