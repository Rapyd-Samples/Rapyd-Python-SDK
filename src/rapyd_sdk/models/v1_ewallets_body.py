from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .v1ewallets_contact import V1ewalletsContact


@JsonMap({"type_": "type"})
class V1EwalletsBody(BaseModel):
    """V1EwalletsBody

    :param contact: contact
    :type contact: V1ewalletsContact
    :param ewallet_reference_id: Rapyd Wallet ID defined by the customer or end user. Must be unique., defaults to None
    :type ewallet_reference_id: str, optional
    :param first_name: First name of the Rapyd Wallet owner., defaults to None
    :type first_name: str, optional
    :param last_name: Last name of the Rapyd Wallet owner., defaults to None
    :type last_name: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param type_: Type of wallet, company or person. Default is person., defaults to None
    :type type_: str, optional
    """

    def __init__(
        self,
        contact: V1ewalletsContact,
        ewallet_reference_id: str = None,
        first_name: str = None,
        last_name: str = None,
        metadata: dict = None,
        type_: str = None,
    ):
        """V1EwalletsBody

        :param contact: contact
        :type contact: V1ewalletsContact
        :param ewallet_reference_id: Rapyd Wallet ID defined by the customer or end user. Must be unique., defaults to None
        :type ewallet_reference_id: str, optional
        :param first_name: First name of the Rapyd Wallet owner., defaults to None
        :type first_name: str, optional
        :param last_name: Last name of the Rapyd Wallet owner., defaults to None
        :type last_name: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param type_: Type of wallet, company or person. Default is person., defaults to None
        :type type_: str, optional
        """
        self.contact = self._define_object(contact, V1ewalletsContact)
        self.ewallet_reference_id = self._define_str(
            "ewallet_reference_id", ewallet_reference_id, nullable=True
        )
        self.first_name = self._define_str("first_name", first_name, nullable=True)
        self.last_name = self._define_str("last_name", last_name, nullable=True)
        self.metadata = metadata
        self.type_ = self._define_str("type_", type_, nullable=True)
