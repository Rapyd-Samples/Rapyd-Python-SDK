from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .card_transaction import CardTransaction


@JsonMap({"id_": "id"})
class InlineResponse200_29Data(BaseModel):
    """InlineResponse200_29Data

    :param bank_account: Issued virtual account., defaults to None
    :type bank_account: dict, optional
    :param country: The country that the account number will be associated with. Two-letter ISO 3166-1 ALPHA-2 code. Uppercase., defaults to None
    :type country: str, optional
    :param currency: Currency of the account. Three-letter ISO 4217 code., defaults to None
    :type currency: str, optional
    :param description: Description of the account., defaults to None
    :type description: str, optional
    :param ewallet: ID of the wallet the bank account number is issued to. String starting with **ewallet_**., defaults to None
    :type ewallet: str, optional
    :param funding_instructions: Issued virtual account funding instructions., defaults to None
    :type funding_instructions: dict, optional
    :param id_: The country that the account number will be associated with. Two-letter ISO 3166-1 ALPHA-2 code. Uppercase., defaults to None
    :type id_: str, optional
    :param merchant_reference_id: ID of this account, as provided by the merchant. Limited to 45 characters., defaults to None
    :type merchant_reference_id: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param status: Issued virtual account statuts., defaults to None
    :type status: str, optional
    :param transactions: Issued virtual account transactions., defaults to None
    :type transactions: List[CardTransaction], optional
    :param requested_currency: *Currency received by the virtual account after conversion. Uppercase. One of the following: AUD - Australian Dollar EUR - Euro GBP - Pound Sterling HKD - Hong Kong Dollar SGD - Singapore Dollar USD - US Dollar When not specified, the funds appear in the wallet’s currency account for the currency of the transaction.*, defaults to None
    :type requested_currency: str, optional
    """

    def __init__(
        self,
        bank_account: dict = None,
        country: str = None,
        currency: str = None,
        description: str = None,
        ewallet: str = None,
        funding_instructions: dict = None,
        id_: str = None,
        merchant_reference_id: str = None,
        metadata: dict = None,
        status: str = None,
        transactions: List[CardTransaction] = None,
        requested_currency: str = None,
    ):
        """InlineResponse200_29Data

        :param bank_account: Issued virtual account., defaults to None
        :type bank_account: dict, optional
        :param country: The country that the account number will be associated with. Two-letter ISO 3166-1 ALPHA-2 code. Uppercase., defaults to None
        :type country: str, optional
        :param currency: Currency of the account. Three-letter ISO 4217 code., defaults to None
        :type currency: str, optional
        :param description: Description of the account., defaults to None
        :type description: str, optional
        :param ewallet: ID of the wallet the bank account number is issued to. String starting with **ewallet_**., defaults to None
        :type ewallet: str, optional
        :param funding_instructions: Issued virtual account funding instructions., defaults to None
        :type funding_instructions: dict, optional
        :param id_: The country that the account number will be associated with. Two-letter ISO 3166-1 ALPHA-2 code. Uppercase., defaults to None
        :type id_: str, optional
        :param merchant_reference_id: ID of this account, as provided by the merchant. Limited to 45 characters., defaults to None
        :type merchant_reference_id: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param status: Issued virtual account statuts., defaults to None
        :type status: str, optional
        :param transactions: Issued virtual account transactions., defaults to None
        :type transactions: List[CardTransaction], optional
        :param requested_currency: *Currency received by the virtual account after conversion. Uppercase. One of the following: AUD - Australian Dollar EUR - Euro GBP - Pound Sterling HKD - Hong Kong Dollar SGD - Singapore Dollar USD - US Dollar When not specified, the funds appear in the wallet’s currency account for the currency of the transaction.*, defaults to None
        :type requested_currency: str, optional
        """
        self.bank_account = bank_account
        self.country = self._define_str("country", country, nullable=True)
        self.currency = self._define_str("currency", currency, nullable=True)
        self.description = self._define_str("description", description, nullable=True)
        self.ewallet = self._define_str("ewallet", ewallet, nullable=True)
        self.funding_instructions = funding_instructions
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.merchant_reference_id = self._define_str(
            "merchant_reference_id", merchant_reference_id, nullable=True
        )
        self.metadata = metadata
        self.status = self._define_str("status", status, nullable=True)
        self.transactions = self._define_list(transactions, CardTransaction)
        self.requested_currency = self._define_str(
            "requested_currency", requested_currency, nullable=True
        )
