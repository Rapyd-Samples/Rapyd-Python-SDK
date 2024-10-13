from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class CardTokenResponsePaymentParams(BaseModel):
    """Contains the following fields. When these fields do not include values, the user is redirected to the hosted page, and a related status message appears at the top of the page.

    :param complete_payment_url: URL where the customer is redirected when payment is successful, after returning from an external page such as a 3DS page. Does not support localhost URLs., defaults to None
    :type complete_payment_url: str, optional
    :param error_payment_url: URL where the customer is redirected when payment is not successful, after returning from an external page, such as a 3DS page. Does not support localhost URLs., defaults to None
    :type error_payment_url: str, optional
    """

    def __init__(self, complete_payment_url: str = None, error_payment_url: str = None):
        """Contains the following fields. When these fields do not include values, the user is redirected to the hosted page, and a related status message appears at the top of the page.

        :param complete_payment_url: URL where the customer is redirected when payment is successful, after returning from an external page such as a 3DS page. Does not support localhost URLs., defaults to None
        :type complete_payment_url: str, optional
        :param error_payment_url: URL where the customer is redirected when payment is not successful, after returning from an external page, such as a 3DS page. Does not support localhost URLs., defaults to None
        :type error_payment_url: str, optional
        """
        self.complete_payment_url = self._define_str(
            "complete_payment_url", complete_payment_url, nullable=True
        )
        self.error_payment_url = self._define_str(
            "error_payment_url", error_payment_url, nullable=True
        )
