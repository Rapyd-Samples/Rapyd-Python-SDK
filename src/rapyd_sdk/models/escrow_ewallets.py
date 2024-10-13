from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class EscrowEwallets(BaseModel):
    """Describes the wallets and the releases from escrow.

    :param ewallet: ID of the wallet, a string starting with **ewallet_**., defaults to None
    :type ewallet: str, optional
    :param amount: The amount to release to this wallet. Relevant when `percentage` is not set., defaults to None
    :type amount: float, optional
    :param percentage: The percentage of this escrow to release to this wallet. Relevant when `amount` is not set. On a partial release after the first, this refers to the percentage of the original amount of the escrow., defaults to None
    :type percentage: float, optional
    """

    def __init__(
        self, ewallet: str = None, amount: float = None, percentage: float = None
    ):
        """Describes the wallets and the releases from escrow.

        :param ewallet: ID of the wallet, a string starting with **ewallet_**., defaults to None
        :type ewallet: str, optional
        :param amount: The amount to release to this wallet. Relevant when `percentage` is not set., defaults to None
        :type amount: float, optional
        :param percentage: The percentage of this escrow to release to this wallet. Relevant when `amount` is not set. On a partial release after the first, this refers to the percentage of the original amount of the escrow., defaults to None
        :type percentage: float, optional
        """
        self.ewallet = self._define_str("ewallet", ewallet, nullable=True)
        self.amount = self._define_number("amount", amount, nullable=True)
        self.percentage = self._define_number("percentage", percentage, nullable=True)
