from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class EwalletsEwalletTokenBody(BaseModel):
    """EwalletsEwalletTokenBody

    :param ewallet_reference_id: Rapyd Wallet ID defined by the customer or end user.  Must be unique., defaults to None
    :type ewallet_reference_id: str, optional
    :param first_name: First name of the Rapyd Wallet owner., defaults to None
    :type first_name: str, optional
    :param last_name: Last name of the Rapyd Wallet owner., defaults to None
    :type last_name: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    """

    def __init__(
        self,
        ewallet_reference_id: str = None,
        first_name: str = None,
        last_name: str = None,
        metadata: dict = None,
    ):
        """EwalletsEwalletTokenBody

        :param ewallet_reference_id: Rapyd Wallet ID defined by the customer or end user.  Must be unique., defaults to None
        :type ewallet_reference_id: str, optional
        :param first_name: First name of the Rapyd Wallet owner., defaults to None
        :type first_name: str, optional
        :param last_name: Last name of the Rapyd Wallet owner., defaults to None
        :type last_name: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        """
        self.ewallet_reference_id = self._define_str(
            "ewallet_reference_id", ewallet_reference_id, nullable=True
        )
        self.first_name = self._define_str("first_name", first_name, nullable=True)
        self.last_name = self._define_str("last_name", last_name, nullable=True)
        self.metadata = metadata
