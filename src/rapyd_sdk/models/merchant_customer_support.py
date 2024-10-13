from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class MerchantCustomerSupport(BaseModel):
    """Contains details of the client’s customer support. To configure these fields, use the Client Portal.

    :param email: Email address., defaults to None
    :type email: str, optional
    :param url: URL for the client's customer support service., defaults to None
    :type url: str, optional
    :param phone_number: Phone number for contacting the client's customer support service., defaults to None
    :type phone_number: str, optional
    :param merchant_logo: URL for the image of the client's logo. To configure this field, use the Client Portal., defaults to None
    :type merchant_logo: str, optional
    """

    def __init__(
        self,
        email: str = None,
        url: str = None,
        phone_number: str = None,
        merchant_logo: str = None,
    ):
        """Contains details of the client’s customer support. To configure these fields, use the Client Portal.

        :param email: Email address., defaults to None
        :type email: str, optional
        :param url: URL for the client's customer support service., defaults to None
        :type url: str, optional
        :param phone_number: Phone number for contacting the client's customer support service., defaults to None
        :type phone_number: str, optional
        :param merchant_logo: URL for the image of the client's logo. To configure this field, use the Client Portal., defaults to None
        :type merchant_logo: str, optional
        """
        self.email = self._define_str("email", email, nullable=True)
        self.url = self._define_str("url", url, nullable=True)
        self.phone_number = self._define_str(
            "phone_number", phone_number, nullable=True
        )
        self.merchant_logo = self._define_str(
            "merchant_logo", merchant_logo, nullable=True
        )
