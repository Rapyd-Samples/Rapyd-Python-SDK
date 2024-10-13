from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class GroupPayment(BaseModel):
    """Group Payment

    :param amount: Amount of the group payment, in units defined by `currency`., defaults to None
    :type amount: float, optional
    :param amount_to_replace: Indicates the total amount of failed payments that have not been replaced., defaults to None
    :type amount_to_replace: str, optional
    :param cancel_reason: Reason for cancellation of the group payment., defaults to None
    :type cancel_reason: str, optional
    :param country: Country where the payment methods are supported. Two-letter ISO 3166-1 ALPHA-2 code., defaults to None
    :type country: str, optional
    :param currency: Currency of the payments. Three-letter ISO 4217 code., defaults to None
    :type currency: str, optional
    :param description: Description of the group payment., defaults to None
    :type description: str, optional
    :param expiration: End of the time allowed for customers to make this payment, in Unix time., defaults to None
    :type expiration: float, optional
    :param id_: ID of the 'group_payment' object. String starting with **gp_**., defaults to None
    :type id_: str, optional
    :param merchant_reference_id: Identifier defined by the client for reference purposes. Limit: 45 characters., defaults to None
    :type merchant_reference_id: str, optional
    :param metadata: A JSON object defined by the client, defaults to None
    :type metadata: dict, optional
    :param payments: Array of `payment` objects. All payments must have the same currency and must be supported in the same country. For details of the fields in the 'payment' object., defaults to None
    :type payments: dict, optional
    :param reason: Reason for cancellation of the group payment., defaults to None
    :type reason: str, optional
    :param status: Indicates the status of the group payment operation. One of the following values: <BR>> * **active** - The group payment was created and one or more payments are still open.<BR> * **canceled** - The group payment was canceled. <BR>* **closed** - All payments in the group payment are complete.Response only., defaults to None
    :type status: str, optional
    """

    def __init__(
        self,
        amount: float = None,
        amount_to_replace: str = None,
        cancel_reason: str = None,
        country: str = None,
        currency: str = None,
        description: str = None,
        expiration: float = None,
        id_: str = None,
        merchant_reference_id: str = None,
        metadata: dict = None,
        payments: dict = None,
        reason: str = None,
        status: str = None,
    ):
        """Group Payment

        :param amount: Amount of the group payment, in units defined by `currency`., defaults to None
        :type amount: float, optional
        :param amount_to_replace: Indicates the total amount of failed payments that have not been replaced., defaults to None
        :type amount_to_replace: str, optional
        :param cancel_reason: Reason for cancellation of the group payment., defaults to None
        :type cancel_reason: str, optional
        :param country: Country where the payment methods are supported. Two-letter ISO 3166-1 ALPHA-2 code., defaults to None
        :type country: str, optional
        :param currency: Currency of the payments. Three-letter ISO 4217 code., defaults to None
        :type currency: str, optional
        :param description: Description of the group payment., defaults to None
        :type description: str, optional
        :param expiration: End of the time allowed for customers to make this payment, in Unix time., defaults to None
        :type expiration: float, optional
        :param id_: ID of the 'group_payment' object. String starting with **gp_**., defaults to None
        :type id_: str, optional
        :param merchant_reference_id: Identifier defined by the client for reference purposes. Limit: 45 characters., defaults to None
        :type merchant_reference_id: str, optional
        :param metadata: A JSON object defined by the client, defaults to None
        :type metadata: dict, optional
        :param payments: Array of `payment` objects. All payments must have the same currency and must be supported in the same country. For details of the fields in the 'payment' object., defaults to None
        :type payments: dict, optional
        :param reason: Reason for cancellation of the group payment., defaults to None
        :type reason: str, optional
        :param status: Indicates the status of the group payment operation. One of the following values: <BR>> * **active** - The group payment was created and one or more payments are still open.<BR> * **canceled** - The group payment was canceled. <BR>* **closed** - All payments in the group payment are complete.Response only., defaults to None
        :type status: str, optional
        """
        self.amount = self._define_number("amount", amount, nullable=True)
        self.amount_to_replace = self._define_str(
            "amount_to_replace", amount_to_replace, nullable=True
        )
        self.cancel_reason = self._define_str(
            "cancel_reason", cancel_reason, nullable=True
        )
        self.country = self._define_str("country", country, nullable=True)
        self.currency = self._define_str("currency", currency, nullable=True)
        self.description = self._define_str("description", description, nullable=True)
        self.expiration = self._define_number("expiration", expiration, nullable=True)
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.merchant_reference_id = self._define_str(
            "merchant_reference_id", merchant_reference_id, nullable=True
        )
        self.metadata = metadata
        self.payments = payments
        self.reason = self._define_str("reason", reason, nullable=True)
        self.status = self._define_str("status", status, nullable=True)
