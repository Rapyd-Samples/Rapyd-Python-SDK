from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .escrow_ewallets import EscrowEwallets


@JsonMap({})
class EscrowEscrowReleasesBody(BaseModel):
    """EscrowEscrowReleasesBody

    :param ewallets: Describes the wallets and the releases from escrow.
    :type ewallets: EscrowEwallets
    """

    def __init__(self, ewallets: EscrowEwallets):
        """EscrowEscrowReleasesBody

        :param ewallets: Describes the wallets and the releases from escrow.
        :type ewallets: EscrowEwallets
        """
        self.ewallets = self._define_object(ewallets, EscrowEwallets)
