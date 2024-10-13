from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .escrow_ewallets import EscrowEwallets


@JsonMap({"id_": "id"})
class EscrowResponseEscrowReleasesData(BaseModel):
    """Array of objects that describe individual escrow releases.

    :param amount: The currency of the escrow balance. Three-letter ISO 4217 code., defaults to None
    :type amount: float, optional
    :param created_at: Date and time the escrow release was created, in Unix time., defaults to None
    :type created_at: float, optional
    :param currency: The currency of the escrow balance. Three-letter ISO 4217 code., defaults to None
    :type currency: str, optional
    :param ewallets: Describes the wallets and the releases from escrow., defaults to None
    :type ewallets: EscrowEwallets, optional
    :param id_: ID of the escrow release, a string starting with **er_**., defaults to None
    :type id_: float, optional
    :param proportional_release: Indicates that the wallets were released in the same proportion that was defined in the Create Payment request., defaults to None
    :type proportional_release: bool, optional
    :param trigger: Indicates what triggered the escrow release. One of the following: <BR> * **event** - Funds were released due to an API request. <BR> **time** - Funds were automatically released at 5:00 p.m. GMT (17:00 GMT) on the day indicated in theCreate Payment request. <BR> **cancel_escrow** - Escrow was canceled., defaults to None
    :type trigger: str, optional
    """

    def __init__(
        self,
        amount: float = None,
        created_at: float = None,
        currency: str = None,
        ewallets: EscrowEwallets = None,
        id_: float = None,
        proportional_release: bool = None,
        trigger: str = None,
    ):
        """Array of objects that describe individual escrow releases.

        :param amount: The currency of the escrow balance. Three-letter ISO 4217 code., defaults to None
        :type amount: float, optional
        :param created_at: Date and time the escrow release was created, in Unix time., defaults to None
        :type created_at: float, optional
        :param currency: The currency of the escrow balance. Three-letter ISO 4217 code., defaults to None
        :type currency: str, optional
        :param ewallets: Describes the wallets and the releases from escrow., defaults to None
        :type ewallets: EscrowEwallets, optional
        :param id_: ID of the escrow release, a string starting with **er_**., defaults to None
        :type id_: float, optional
        :param proportional_release: Indicates that the wallets were released in the same proportion that was defined in the Create Payment request., defaults to None
        :type proportional_release: bool, optional
        :param trigger: Indicates what triggered the escrow release. One of the following: <BR> * **event** - Funds were released due to an API request. <BR> **time** - Funds were automatically released at 5:00 p.m. GMT (17:00 GMT) on the day indicated in theCreate Payment request. <BR> **cancel_escrow** - Escrow was canceled., defaults to None
        :type trigger: str, optional
        """
        self.amount = self._define_number("amount", amount, nullable=True)
        self.created_at = self._define_number("created_at", created_at, nullable=True)
        self.currency = self._define_str("currency", currency, nullable=True)
        self.ewallets = self._define_object(ewallets, EscrowEwallets)
        self.id_ = self._define_number("id_", id_, nullable=True)
        self.proportional_release = proportional_release
        self.trigger = self._define_str("trigger", trigger, nullable=True)
