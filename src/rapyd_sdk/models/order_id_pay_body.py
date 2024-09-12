from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class OrderIdPayBody(BaseModel):
    """OrderIdPayBody

    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param payment_method: ID of the payment method. String starting with card_ or other_. If not specified, the payment method is the default_payment_method of the customer., defaults to None
    :type payment_method: str, optional
    :param customer: ID of a customer. String starting with cus_. The order is paid with the customer's default payment method., defaults to None
    :type customer: str, optional
    """

    def __init__(
        self, metadata: dict = None, payment_method: str = None, customer: str = None
    ):
        """OrderIdPayBody

        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param payment_method: ID of the payment method. String starting with card_ or other_. If not specified, the payment method is the default_payment_method of the customer., defaults to None
        :type payment_method: str, optional
        :param customer: ID of a customer. String starting with cus_. The order is paid with the customer's default payment method., defaults to None
        :type customer: str, optional
        """
        self.metadata = metadata
        self.payment_method = self._define_str(
            "payment_method", payment_method, nullable=True
        )
        self.customer = self._define_str("customer", customer, nullable=True)
