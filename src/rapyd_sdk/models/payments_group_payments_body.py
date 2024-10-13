from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class PaymentsGroupPaymentsBody(BaseModel):
    """PaymentsGroupPaymentsBody

    :param description: Description of the group payment, defaults to None
    :type description: str, optional
    :param merchant_reference_id: ID defined by the client. Limited to 255 characters., defaults to None
    :type merchant_reference_id: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param payments: Array of 'payment' objects. For details about the fields in the 'payment' object, see [Create Payment](https://docs.rapyd.net/en/create-payment.html).
    :type payments: dict
    """

    def __init__(
        self,
        payments: dict,
        description: str = None,
        merchant_reference_id: str = None,
        metadata: dict = None,
    ):
        """PaymentsGroupPaymentsBody

        :param description: Description of the group payment, defaults to None
        :type description: str, optional
        :param merchant_reference_id: ID defined by the client. Limited to 255 characters., defaults to None
        :type merchant_reference_id: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param payments: Array of 'payment' objects. For details about the fields in the 'payment' object, see [Create Payment](https://docs.rapyd.net/en/create-payment.html).
        :type payments: dict
        """
        self.description = self._define_str("description", description, nullable=True)
        self.merchant_reference_id = self._define_str(
            "merchant_reference_id", merchant_reference_id, nullable=True
        )
        self.metadata = metadata
        self.payments = payments
