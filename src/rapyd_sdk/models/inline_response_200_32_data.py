from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .inline_response_200_30_data_transactions import (
    InlineResponse200_30DataTransactions,
)


@JsonMap({"id_": "id"})
class InlineResponse200_32Data(BaseModel):
    """InlineResponse200_32Data

    :param id_: ID of the issued card transaction object. String starting with **cit_**., defaults to None
    :type id_: str, optional
    :param merchant_reference_id: ID of this account, as provided by the merchant. Limited to 45 characters., defaults to None
    :type merchant_reference_id: str, optional
    :param ewallet: ID of the wallet the bank account number is issued to. String starting with **ewallet_**., defaults to None
    :type ewallet: str, optional
    :param bank_account: Issued virtual account., defaults to None
    :type bank_account: dict, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param status: Issued virtual account statuts., defaults to None
    :type status: str, optional
    :param description: Description of the account., defaults to None
    :type description: str, optional
    :param funding_instructions: Issued virtual account funding instructions., defaults to None
    :type funding_instructions: dict, optional
    :param currency: Currency of the transaction. Three-letter ISO 4217., defaults to None
    :type currency: str, optional
    :param transactions: Issued virtual account transactions., defaults to None
    :type transactions: List[InlineResponse200_30DataTransactions], optional
    """

    def __init__(
        self,
        id_: str = None,
        merchant_reference_id: str = None,
        ewallet: str = None,
        bank_account: dict = None,
        metadata: dict = None,
        status: str = None,
        description: str = None,
        funding_instructions: dict = None,
        currency: str = None,
        transactions: List[InlineResponse200_30DataTransactions] = None,
    ):
        """InlineResponse200_32Data

        :param id_: ID of the issued card transaction object. String starting with **cit_**., defaults to None
        :type id_: str, optional
        :param merchant_reference_id: ID of this account, as provided by the merchant. Limited to 45 characters., defaults to None
        :type merchant_reference_id: str, optional
        :param ewallet: ID of the wallet the bank account number is issued to. String starting with **ewallet_**., defaults to None
        :type ewallet: str, optional
        :param bank_account: Issued virtual account., defaults to None
        :type bank_account: dict, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param status: Issued virtual account statuts., defaults to None
        :type status: str, optional
        :param description: Description of the account., defaults to None
        :type description: str, optional
        :param funding_instructions: Issued virtual account funding instructions., defaults to None
        :type funding_instructions: dict, optional
        :param currency: Currency of the transaction. Three-letter ISO 4217., defaults to None
        :type currency: str, optional
        :param transactions: Issued virtual account transactions., defaults to None
        :type transactions: List[InlineResponse200_30DataTransactions], optional
        """
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.merchant_reference_id = self._define_str(
            "merchant_reference_id", merchant_reference_id, nullable=True
        )
        self.ewallet = self._define_str("ewallet", ewallet, nullable=True)
        self.bank_account = bank_account
        self.metadata = metadata
        self.status = self._define_str("status", status, nullable=True)
        self.description = self._define_str("description", description, nullable=True)
        self.funding_instructions = funding_instructions
        self.currency = self._define_str("currency", currency, nullable=True)
        self.transactions = self._define_list(
            transactions, InlineResponse200_30DataTransactions
        )
