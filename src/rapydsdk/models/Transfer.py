from enum import Enum
from .utils.JsonMap import JsonMap
from .base import BaseModel


class Status1(Enum):
    CAN = "CAN"
    CLO = "CLO"
    DEC = "DEC"
    EXP = "EXP"
    HLD = "HLD"
    PEN = "PEN"
    REJ = "REJ"

    def list():
        return list(map(lambda x: x.value, Status1._member_map_.values()))


@JsonMap({})
class Transfer(BaseModel):
    def __init__(
        self,
        amount: float = None,
        created_at: float = None,
        currency_code: str = None,
        destination_ewallet_id: str = None,
        destination_phone_number: str = None,
        destination_transaction_id: str = None,
        id: str = None,
        metadata: dict = None,
        response_metadata: dict = None,
        source_ewallet_id: str = None,
        source_transaction_id: str = None,
        status: Status1 = None,
        transfer_response_at: float = None,
        expiration: float = None,
    ):
        self.amount = amount
        self.created_at = created_at
        self.currency_code = currency_code
        self.destination_ewallet_id = destination_ewallet_id
        self.destination_phone_number = destination_phone_number
        self.destination_transaction_id = destination_transaction_id
        self.id = id
        self.metadata = metadata
        self.response_metadata = response_metadata
        self.source_ewallet_id = source_ewallet_id
        self.source_transaction_id = source_transaction_id
        self.status = (
            self._enum_matching(status, Status1.list(), "status") if status else None
        )
        self.transfer_response_at = transfer_response_at
        self.expiration = expiration
