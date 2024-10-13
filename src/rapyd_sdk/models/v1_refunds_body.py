from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class V1RefundsBody(BaseModel):
    """V1RefundsBody

    :param amount: The amount of the refund. Decimal., defaults to None
    :type amount: float, optional
    :param currency: The currency of the amount received by the original payment source. Three-letter ISO 4217 code., defaults to None
    :type currency: str, optional
    :param ewallets: ID of the wallet contact that the card is assigned to. String starting with **cont_**., defaults to None
    :type ewallets: List[str], optional
    :param merchant_reference_id: ID defined by the client. Limited to 255 characters., defaults to None
    :type merchant_reference_id: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param payment: ID of the Payment object that the refund is charged against. String starting with **payment_**.
    :type payment: str
    :param reason: Description of the reason for the refund., defaults to None
    :type reason: str, optional
    """

    def __init__(
        self,
        payment: str,
        amount: float = None,
        currency: str = None,
        ewallets: List[str] = None,
        merchant_reference_id: str = None,
        metadata: dict = None,
        reason: str = None,
    ):
        """V1RefundsBody

        :param amount: The amount of the refund. Decimal., defaults to None
        :type amount: float, optional
        :param currency: The currency of the amount received by the original payment source. Three-letter ISO 4217 code., defaults to None
        :type currency: str, optional
        :param ewallets: ID of the wallet contact that the card is assigned to. String starting with **cont_**., defaults to None
        :type ewallets: List[str], optional
        :param merchant_reference_id: ID defined by the client. Limited to 255 characters., defaults to None
        :type merchant_reference_id: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param payment: ID of the Payment object that the refund is charged against. String starting with **payment_**.
        :type payment: str
        :param reason: Description of the reason for the refund., defaults to None
        :type reason: str, optional
        """
        self.amount = self._define_number("amount", amount, nullable=True)
        self.currency = self._define_str("currency", currency, nullable=True)
        self.ewallets = ewallets
        self.merchant_reference_id = self._define_str(
            "merchant_reference_id", merchant_reference_id, nullable=True
        )
        self.metadata = metadata
        self.payment = payment
        self.reason = self._define_str("reason", reason, nullable=True)
