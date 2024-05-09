from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .FxFee import FxFee
from .TransactionFee import TransactionFee


@JsonMap({})
class PaymentFee(BaseModel):
    def __init__(
        self,
        fx_fee: FxFee = None,
        gross_fees: float = None,
        net_fees: float = None,
        transaction_fee: TransactionFee = None,
        total_merchant_fees: float = None,
    ):
        self.fx_fee = self._define_object(fx_fee, FxFee)
        self.gross_fees = gross_fees
        self.net_fees = net_fees
        self.transaction_fee = self._define_object(transaction_fee, TransactionFee)
        self.total_merchant_fees = total_merchant_fees
