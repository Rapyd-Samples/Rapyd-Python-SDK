from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .fx_fee import FxFee
from .transaction_fee import TransactionFee


@JsonMap({})
class Fee(BaseModel):
    """Fee

    :param fx_fee: Describes the fees for processing the currency exchange. Relevant to payouts with FX., defaults to None
    :type fx_fee: FxFee, optional
    :param gross_fees: The total gross fees for the transaction, in units defined by currency_code. Relevant to responses., defaults to None
    :type gross_fees: float, optional
    :param net_fees: The total net fees for the transaction, in units defined by merchant_requested_currency. Relevant to responses., defaults to None
    :type net_fees: float, optional
    :param transaction_fee: Describes the fee for processing the transaction., defaults to None
    :type transaction_fee: TransactionFee, optional
    :param total_merchant_fees: total_merchant_fees, defaults to None
    :type total_merchant_fees: float, optional
    """

    def __init__(
        self,
        fx_fee: FxFee = None,
        gross_fees: float = None,
        net_fees: float = None,
        transaction_fee: TransactionFee = None,
        total_merchant_fees: float = None,
    ):
        """Fee

        :param fx_fee: Describes the fees for processing the currency exchange. Relevant to payouts with FX., defaults to None
        :type fx_fee: FxFee, optional
        :param gross_fees: The total gross fees for the transaction, in units defined by currency_code. Relevant to responses., defaults to None
        :type gross_fees: float, optional
        :param net_fees: The total net fees for the transaction, in units defined by merchant_requested_currency. Relevant to responses., defaults to None
        :type net_fees: float, optional
        :param transaction_fee: Describes the fee for processing the transaction., defaults to None
        :type transaction_fee: TransactionFee, optional
        :param total_merchant_fees: total_merchant_fees, defaults to None
        :type total_merchant_fees: float, optional
        """
        self.fx_fee = self._define_object(fx_fee, FxFee)
        self.gross_fees = self._define_number("gross_fees", gross_fees, nullable=True)
        self.net_fees = self._define_number("net_fees", net_fees, nullable=True)
        self.transaction_fee = self._define_object(transaction_fee, TransactionFee)
        self.total_merchant_fees = self._define_number(
            "total_merchant_fees", total_merchant_fees, nullable=True
        )
