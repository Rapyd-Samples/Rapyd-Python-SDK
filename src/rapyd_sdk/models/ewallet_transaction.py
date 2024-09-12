from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class EwalletTransactionBalanceType(Enum):
    """An enumeration representing different categories.

    :cvar AVAILABLEBALANCE: "available_balance"
    :vartype AVAILABLEBALANCE: str
    :cvar ONHOLDBALANCE: "on_hold_balance"
    :vartype ONHOLDBALANCE: str
    :cvar RECEIVEDBALANCE: "received_balance"
    :vartype RECEIVEDBALANCE: str
    :cvar RESERVEBALANCE: "reserve_balance"
    :vartype RESERVEBALANCE: str
    """

    AVAILABLEBALANCE = "available_balance"
    ONHOLDBALANCE = "on_hold_balance"
    RECEIVEDBALANCE = "received_balance"
    RESERVEBALANCE = "reserve_balance"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, EwalletTransactionBalanceType._member_map_.values())
        )


class EwalletTransactionDestinationBalanceType(Enum):
    """An enumeration representing different categories.

    :cvar AVAILABLEBALANCE: "available_balance"
    :vartype AVAILABLEBALANCE: str
    :cvar ONHOLDBALANCE: "on_hold_balance"
    :vartype ONHOLDBALANCE: str
    :cvar RECEIVEDBALANCE: "received_balance"
    :vartype RECEIVEDBALANCE: str
    :cvar RESERVEBALANCE: "reserve_balance"
    :vartype RESERVEBALANCE: str
    """

    AVAILABLEBALANCE = "available_balance"
    ONHOLDBALANCE = "on_hold_balance"
    RECEIVEDBALANCE = "received_balance"
    RESERVEBALANCE = "reserve_balance"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                EwalletTransactionDestinationBalanceType._member_map_.values(),
            )
        )


class EwalletTransactionSourceBalanceType(Enum):
    """An enumeration representing different categories.

    :cvar AVAILABLEBALANCE: "available_balance"
    :vartype AVAILABLEBALANCE: str
    :cvar ONHOLDBALANCE: "on_hold_balance"
    :vartype ONHOLDBALANCE: str
    :cvar RECEIVEDBALANCE: "received_balance"
    :vartype RECEIVEDBALANCE: str
    :cvar RESERVEBALANCE: "reserve_balance"
    :vartype RESERVEBALANCE: str
    """

    AVAILABLEBALANCE = "available_balance"
    ONHOLDBALANCE = "on_hold_balance"
    RECEIVEDBALANCE = "received_balance"
    RESERVEBALANCE = "reserve_balance"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                EwalletTransactionSourceBalanceType._member_map_.values(),
            )
        )


@JsonMap({"id_": "id", "type_": "type"})
class EwalletTransaction(BaseModel):
    """EwalletTransaction

    :param metadata: metadata, defaults to None
    :type metadata: dict, optional
    :param amount: Amount of the transaction, in units of the currency defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 4217:2015., defaults to None
    :type amount: float, optional
    :param balance: The updated wallet balance after successful completion of the transaction., defaults to None
    :type balance: float, optional
    :param balance_type: Balance type affected by the transaction. One of the following, defaults to None
    :type balance_type: EwalletTransactionBalanceType, optional
    :param created_at: Time the transaction was made, in Unix time., defaults to None
    :type created_at: float, optional
    :param currency: Three-letter ISO 4217 code for the currency used in the amount field., defaults to None
    :type currency: str, optional
    :param destination_balance_type: The destination balance type when funds are transferred from one balance to another within the wallet, defaults to None
    :type destination_balance_type: EwalletTransactionDestinationBalanceType, optional
    :param ewallet_id: ID of the wallet. String starting with ewallet_., defaults to None
    :type ewallet_id: str, optional
    :param id_: ID of the transaction. String starting with wt_ or UUID., defaults to None
    :type id_: str, optional
    :param reason: Unique identifier of the wallet object. String starting with ewallet_., defaults to None
    :type reason: str, optional
    :param source_balance_type: The source balance type when funds are transferred from one balance to another within the wallet, defaults to None
    :type source_balance_type: EwalletTransactionSourceBalanceType, optional
    :param status: Status of the transaction., defaults to None
    :type status: str, optional
    :param type_: Type of transaction, defaults to None
    :type type_: str, optional
    :param subtype: Subtype of the transaction., defaults to None
    :type subtype: float, optional
    :param action_data: action_data, defaults to None
    :type action_data: dict, optional
    """

    def __init__(
        self,
        metadata: dict = None,
        amount: float = None,
        balance: float = None,
        balance_type: EwalletTransactionBalanceType = None,
        created_at: float = None,
        currency: str = None,
        destination_balance_type: EwalletTransactionDestinationBalanceType = None,
        ewallet_id: str = None,
        id_: str = None,
        reason: str = None,
        source_balance_type: EwalletTransactionSourceBalanceType = None,
        status: str = None,
        type_: str = None,
        subtype: float = None,
        action_data: dict = None,
    ):
        """EwalletTransaction

        :param metadata: metadata, defaults to None
        :type metadata: dict, optional
        :param amount: Amount of the transaction, in units of the currency defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 4217:2015., defaults to None
        :type amount: float, optional
        :param balance: The updated wallet balance after successful completion of the transaction., defaults to None
        :type balance: float, optional
        :param balance_type: Balance type affected by the transaction. One of the following, defaults to None
        :type balance_type: EwalletTransactionBalanceType, optional
        :param created_at: Time the transaction was made, in Unix time., defaults to None
        :type created_at: float, optional
        :param currency: Three-letter ISO 4217 code for the currency used in the amount field., defaults to None
        :type currency: str, optional
        :param destination_balance_type: The destination balance type when funds are transferred from one balance to another within the wallet, defaults to None
        :type destination_balance_type: EwalletTransactionDestinationBalanceType, optional
        :param ewallet_id: ID of the wallet. String starting with ewallet_., defaults to None
        :type ewallet_id: str, optional
        :param id_: ID of the transaction. String starting with wt_ or UUID., defaults to None
        :type id_: str, optional
        :param reason: Unique identifier of the wallet object. String starting with ewallet_., defaults to None
        :type reason: str, optional
        :param source_balance_type: The source balance type when funds are transferred from one balance to another within the wallet, defaults to None
        :type source_balance_type: EwalletTransactionSourceBalanceType, optional
        :param status: Status of the transaction., defaults to None
        :type status: str, optional
        :param type_: Type of transaction, defaults to None
        :type type_: str, optional
        :param subtype: Subtype of the transaction., defaults to None
        :type subtype: float, optional
        :param action_data: action_data, defaults to None
        :type action_data: dict, optional
        """
        self.metadata = metadata
        self.amount = self._define_number("amount", amount, nullable=True)
        self.balance = self._define_number("balance", balance, nullable=True)
        self.balance_type = (
            self._enum_matching(
                balance_type, EwalletTransactionBalanceType.list(), "balance_type"
            )
            if balance_type
            else None
        )
        self.created_at = self._define_number("created_at", created_at, nullable=True)
        self.currency = self._define_str("currency", currency, nullable=True)
        self.destination_balance_type = (
            self._enum_matching(
                destination_balance_type,
                EwalletTransactionDestinationBalanceType.list(),
                "destination_balance_type",
            )
            if destination_balance_type
            else None
        )
        self.ewallet_id = self._define_str("ewallet_id", ewallet_id, nullable=True)
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.reason = self._define_str("reason", reason, nullable=True)
        self.source_balance_type = (
            self._enum_matching(
                source_balance_type,
                EwalletTransactionSourceBalanceType.list(),
                "source_balance_type",
            )
            if source_balance_type
            else None
        )
        self.status = self._define_str("status", status, nullable=True)
        self.type_ = self._define_str("type_", type_, nullable=True)
        self.subtype = self._define_number("subtype", subtype, nullable=True)
        self.action_data = action_data
