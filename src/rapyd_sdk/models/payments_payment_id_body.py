from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .address import Address


@JsonMap({})
class PaymentsPaymentIdBody(BaseModel):
    """PaymentsPaymentIdBody

    :param address: address associated with this specific Rapyd entity Payment/Customer etc..., defaults to None
    :type address: Address, optional
    :param description: Description of the payment., defaults to None
    :type description: str, optional
    :param escrow: To release escrow funds immediately, set to false. If there are multiple sellers, the funds are released to all of them. Relevant to payments with escrow., defaults to None
    :type escrow: bool, optional
    :param escrow_release_days: Defines the number of days after the creation of the payment that the funds are automatically released. Relevant when escrow is true., defaults to None
    :type escrow_release_days: int, optional
    :param initiation_type: Category of transaction initiation type., defaults to None
    :type initiation_type: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param receipt_email: Email address that the receipt for this transaction is sent to., defaults to None
    :type receipt_email: str, optional
    """

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
        """PaymentsPaymentIdBody

        :param address: address associated with this specific Rapyd entity Payment/Customer etc..., defaults to None
        :type address: Address, optional
        :param description: Description of the payment., defaults to None
        :type description: str, optional
        :param escrow: To release escrow funds immediately, set to false. If there are multiple sellers, the funds are released to all of them. Relevant to payments with escrow., defaults to None
        :type escrow: bool, optional
        :param escrow_release_days: Defines the number of days after the creation of the payment that the funds are automatically released. Relevant when escrow is true., defaults to None
        :type escrow_release_days: int, optional
        :param initiation_type: Category of transaction initiation type., defaults to None
        :type initiation_type: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param receipt_email: Email address that the receipt for this transaction is sent to., defaults to None
        :type receipt_email: str, optional
        """
        self.address = self._define_object(address, Address)
        self.description = self._define_str("description", description, nullable=True)
        self.escrow = escrow
        self.escrow_release_days = self._define_number(
            "escrow_release_days", escrow_release_days, nullable=True
        )
        self.initiation_type = self._define_str(
            "initiation_type", initiation_type, nullable=True
        )
        self.metadata = metadata
        self.receipt_email = self._define_str(
            "receipt_email", receipt_email, nullable=True
        )
