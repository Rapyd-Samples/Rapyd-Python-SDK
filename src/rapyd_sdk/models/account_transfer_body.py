from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class AccountTransferBody(BaseModel):
    """AccountTransferBody

    :param amount: Amount of the transfer. Decimal.
    :type amount: float
    :param currency: Three-letter ISO 4217 code for the currency used in the amount field. Uppercase.
    :type currency: str
    :param destination_ewallet: ID of the wallet receiving the money. String starting with **ewallet_**.
    :type destination_ewallet: str
    :param expiration: Determines the day the ewallet funds transfer expires, in Unix time. Acceptance of the ewallet transfer must be completed before the start of this day. The default setting is 14 days from the date the ewallet transfer was created., defaults to None
    :type expiration: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param source_ewallet: ID of the wallet sending the money. String starting with **ewallet_**.
    :type source_ewallet: str
    """

    def __init__(
        self,
        amount: float,
        currency: str,
        destination_ewallet: str,
        source_ewallet: str,
        expiration: str = None,
        metadata: dict = None,
    ):
        """AccountTransferBody

        :param amount: Amount of the transfer. Decimal.
        :type amount: float
        :param currency: Three-letter ISO 4217 code for the currency used in the amount field. Uppercase.
        :type currency: str
        :param destination_ewallet: ID of the wallet receiving the money. String starting with **ewallet_**.
        :type destination_ewallet: str
        :param expiration: Determines the day the ewallet funds transfer expires, in Unix time. Acceptance of the ewallet transfer must be completed before the start of this day. The default setting is 14 days from the date the ewallet transfer was created., defaults to None
        :type expiration: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param source_ewallet: ID of the wallet sending the money. String starting with **ewallet_**.
        :type source_ewallet: str
        """
        self.amount = amount
        self.currency = currency
        self.destination_ewallet = destination_ewallet
        self.expiration = self._define_str("expiration", expiration, nullable=True)
        self.metadata = metadata
        self.source_ewallet = source_ewallet
