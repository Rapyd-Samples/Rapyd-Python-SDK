from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Address import Address


@JsonMap({})
class UpdatePaymentRequest(BaseModel):
    def __init__(
        self,
        address: Address = None,
        description: str = None,
        escrow: bool = None,
        escrow_release_days: int = None,
        initiation_type: str = None,
        metadata: dict = None,
        receipt_email: str = None,
    ):
        self.address = self._define_object(address, Address)
        self.description = description
        self.escrow = escrow
        self.escrow_release_days = escrow_release_days
        self.initiation_type = initiation_type
        self.metadata = metadata
        self.receipt_email = receipt_email
