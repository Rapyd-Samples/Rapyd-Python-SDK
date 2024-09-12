from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class InvoiceIdPayBody(BaseModel):
    """InvoiceIdPayBody

    :param payment_method: ID of the payment method for paying the invoice. If not included in the body, then the customer's default_payment_method is used., defaults to None
    :type payment_method: str, optional
    """

    def __init__(self, payment_method: str = None):
        """InvoiceIdPayBody

        :param payment_method: ID of the payment method for paying the invoice. If not included in the body, then the customer's default_payment_method is used., defaults to None
        :type payment_method: str, optional
        """
        self.payment_method = self._define_str(
            "payment_method", payment_method, nullable=True
        )
