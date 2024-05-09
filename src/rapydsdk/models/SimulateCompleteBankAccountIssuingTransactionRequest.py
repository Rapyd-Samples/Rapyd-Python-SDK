from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class SimulateCompleteBankAccountIssuingTransactionRequest(BaseModel):
    def __init__(self, amount: str, currency: str, issued_bank_account: str):
        self.amount = amount
        self.currency = currency
        self.issued_bank_account = issued_bank_account
