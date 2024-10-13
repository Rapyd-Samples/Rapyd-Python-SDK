from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class BankaccountsBankaccounttransfertobankaccountBody(BaseModel):
    """BankaccountsBankaccounttransfertobankaccountBody

    :param amount: The amount of the transaction, in units of the currency defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015. If the amount is a whole number, use an integer and not a decimal.
    :type amount: str
    :param currency: Currency of the transaction. Three-letter ISO 4217 code. Must be the same as the currency of the virtual account.
    :type currency: str
    :param issued_bank_account: ID of the Virtual Account Number object. String starting with **issuing_**
    :type issued_bank_account: str
    """

    def __init__(self, amount: str, currency: str, issued_bank_account: str):
        """BankaccountsBankaccounttransfertobankaccountBody

        :param amount: The amount of the transaction, in units of the currency defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015. If the amount is a whole number, use an integer and not a decimal.
        :type amount: str
        :param currency: Currency of the transaction. Three-letter ISO 4217 code. Must be the same as the currency of the virtual account.
        :type currency: str
        :param issued_bank_account: ID of the Virtual Account Number object. String starting with **issuing_**
        :type issued_bank_account: str
        """
        self.amount = amount
        self.currency = currency
        self.issued_bank_account = issued_bank_account
