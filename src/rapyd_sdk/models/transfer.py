from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class TransferStatus(Enum):
    """An enumeration representing different categories.

    :cvar CAN: "CAN"
    :vartype CAN: str
    :cvar CLO: "CLO"
    :vartype CLO: str
    :cvar DEC: "DEC"
    :vartype DEC: str
    :cvar EXP: "EXP"
    :vartype EXP: str
    :cvar HLD: "HLD"
    :vartype HLD: str
    :cvar PEN: "PEN"
    :vartype PEN: str
    :cvar REJ: "REJ"
    :vartype REJ: str
    """

    CAN = "CAN"
    CLO = "CLO"
    DEC = "DEC"
    EXP = "EXP"
    HLD = "HLD"
    PEN = "PEN"
    REJ = "REJ"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, TransferStatus._member_map_.values()))


@JsonMap({"id_": "id"})
class Transfer(BaseModel):
    """Transfer

    :param amount: Amount of the transfer. Decimal., defaults to None
    :type amount: float, optional
    :param created_at: Time the transaction was made, in Unix time., defaults to None
    :type created_at: float, optional
    :param currency_code: Three-letter ISO 4217 code for the currency used in the amount field., defaults to None
    :type currency_code: str, optional
    :param destination_ewallet_id: ID of the wallet receiving the money. String starting with ewallet_. Response only., defaults to None
    :type destination_ewallet_id: str, optional
    :param destination_phone_number: Phone number of the owner of the wallet receiving the money, in E.164 format., defaults to None
    :type destination_phone_number: str, optional
    :param destination_transaction_id: ID of the transaction with regard to the destination. String starting with wt_., defaults to None
    :type destination_transaction_id: str, optional
    :param id_: ID of the transaction. String starting with wt_ or UUID., defaults to None
    :type id_: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param response_metadata: Metadata created with Set Transfer Response. Response only., defaults to None
    :type response_metadata: dict, optional
    :param source_ewallet_id: ID of the wallet sending the money. String starting with ewallet_. Response only., defaults to None
    :type source_ewallet_id: str, optional
    :param source_transaction_id: ID of the transaction with regard to the source. String starting with wt_., defaults to None
    :type source_transaction_id: str, optional
    :param status: < Status of the transaction. CAN - Canceled. The transferor canceled the transfer. CLO - Closed. The transferee accepted the funds. DEC - Declined. The transferee rejected the transfer. EXP - Expired. The transferee did not respond before the transfer expired. HLD - Hold. Rapyd Protect is putting this transfer on hold and reviewing it. PEN - Pending. Waiting for the transferee to accept. REJ - Rejected. Rapyd Protect has rejected this transfer., defaults to None
    :type status: TransferStatus, optional
    :param transfer_response_at: Time of the Set Transfer Response operation, in Unix time. Read-only., defaults to None
    :type transfer_response_at: float, optional
    :param expiration: Determines the day the transfer expires, in Unix time. Acceptance of the transfer must occur before the start of this day. Default is 14 days after creation of the transfer., defaults to None
    :type expiration: float, optional
    """

    def __init__(
        self,
        amount: float = None,
        created_at: float = None,
        currency_code: str = None,
        destination_ewallet_id: str = None,
        destination_phone_number: str = None,
        destination_transaction_id: str = None,
        id_: str = None,
        metadata: dict = None,
        response_metadata: dict = None,
        source_ewallet_id: str = None,
        source_transaction_id: str = None,
        status: TransferStatus = None,
        transfer_response_at: float = None,
        expiration: float = None,
    ):
        """Transfer

        :param amount: Amount of the transfer. Decimal., defaults to None
        :type amount: float, optional
        :param created_at: Time the transaction was made, in Unix time., defaults to None
        :type created_at: float, optional
        :param currency_code: Three-letter ISO 4217 code for the currency used in the amount field., defaults to None
        :type currency_code: str, optional
        :param destination_ewallet_id: ID of the wallet receiving the money. String starting with ewallet_. Response only., defaults to None
        :type destination_ewallet_id: str, optional
        :param destination_phone_number: Phone number of the owner of the wallet receiving the money, in E.164 format., defaults to None
        :type destination_phone_number: str, optional
        :param destination_transaction_id: ID of the transaction with regard to the destination. String starting with wt_., defaults to None
        :type destination_transaction_id: str, optional
        :param id_: ID of the transaction. String starting with wt_ or UUID., defaults to None
        :type id_: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param response_metadata: Metadata created with Set Transfer Response. Response only., defaults to None
        :type response_metadata: dict, optional
        :param source_ewallet_id: ID of the wallet sending the money. String starting with ewallet_. Response only., defaults to None
        :type source_ewallet_id: str, optional
        :param source_transaction_id: ID of the transaction with regard to the source. String starting with wt_., defaults to None
        :type source_transaction_id: str, optional
        :param status: < Status of the transaction. CAN - Canceled. The transferor canceled the transfer. CLO - Closed. The transferee accepted the funds. DEC - Declined. The transferee rejected the transfer. EXP - Expired. The transferee did not respond before the transfer expired. HLD - Hold. Rapyd Protect is putting this transfer on hold and reviewing it. PEN - Pending. Waiting for the transferee to accept. REJ - Rejected. Rapyd Protect has rejected this transfer., defaults to None
        :type status: TransferStatus, optional
        :param transfer_response_at: Time of the Set Transfer Response operation, in Unix time. Read-only., defaults to None
        :type transfer_response_at: float, optional
        :param expiration: Determines the day the transfer expires, in Unix time. Acceptance of the transfer must occur before the start of this day. Default is 14 days after creation of the transfer., defaults to None
        :type expiration: float, optional
        """
        self.amount = self._define_number("amount", amount, nullable=True)
        self.created_at = self._define_number("created_at", created_at, nullable=True)
        self.currency_code = self._define_str(
            "currency_code", currency_code, nullable=True
        )
        self.destination_ewallet_id = self._define_str(
            "destination_ewallet_id", destination_ewallet_id, nullable=True
        )
        self.destination_phone_number = self._define_str(
            "destination_phone_number", destination_phone_number, nullable=True
        )
        self.destination_transaction_id = self._define_str(
            "destination_transaction_id", destination_transaction_id, nullable=True
        )
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.metadata = metadata
        self.response_metadata = response_metadata
        self.source_ewallet_id = self._define_str(
            "source_ewallet_id", source_ewallet_id, nullable=True
        )
        self.source_transaction_id = self._define_str(
            "source_transaction_id", source_transaction_id, nullable=True
        )
        self.status = (
            self._enum_matching(status, TransferStatus.list(), "status")
            if status
            else None
        )
        self.transfer_response_at = self._define_number(
            "transfer_response_at", transfer_response_at, nullable=True
        )
        self.expiration = self._define_number("expiration", expiration, nullable=True)
