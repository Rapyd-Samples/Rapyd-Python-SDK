from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .escrow_response_escrow_releases import EscrowResponseEscrowReleases


@JsonMap({"id_": "id"})
class EscrowResponse(BaseModel):
    """EscrowResponse

    :param amount_on_hold: Total amount of funds that are currently held in the escrow, in the currency defined in `currency_code` in the payment., defaults to None
    :type amount_on_hold: float, optional
    :param created_at: Date and time the escrow was created, in Unix time., defaults to None
    :type created_at: float, optional
    :param currency: The currency of the escrow balance. Three-letter ISO 4217 code., defaults to None
    :type currency: float, optional
    :param escrow_releases: Array of objects that describe individual releases., defaults to None
    :type escrow_releases: EscrowResponseEscrowReleases, optional
    :param id_: Indicates that the number of escrow releases is greater than the number returned in the response., defaults to None
    :type id_: str, optional
    :param last_payment_completion: Date and time of the completion of the last payment or partial payment, in Unix time., defaults to None
    :type last_payment_completion: float, optional
    :param payment: ID of the payment, a string starting with **payment_**., defaults to None
    :type payment: float, optional
    :param status: Status of the escrow. One of the following:<BR> * **pending** - The payment and escrow were created, but the payment is not completed and the funds are not in the escrow.<BR> * **on_hold** - The payment is completed and the funds are in escrow. canceled - The escrow is canceled.<BR>* **released** - All or part of the funds have been released to the wallets., defaults to None
    :type status: str, optional
    :param total_amount_released: Total amount of funds that were released to the wallets, in the currency defined in currency_code in the payment response., defaults to None
    :type total_amount_released: str, optional
    :param updated_at: Date and time of the last update to the escrow, in Unix time., defaults to None
    :type updated_at: float, optional
    """

    def __init__(
        self,
        amount_on_hold: float = None,
        created_at: float = None,
        currency: float = None,
        escrow_releases: EscrowResponseEscrowReleases = None,
        id_: str = None,
        last_payment_completion: float = None,
        payment: float = None,
        status: str = None,
        total_amount_released: str = None,
        updated_at: float = None,
    ):
        """EscrowResponse

        :param amount_on_hold: Total amount of funds that are currently held in the escrow, in the currency defined in `currency_code` in the payment., defaults to None
        :type amount_on_hold: float, optional
        :param created_at: Date and time the escrow was created, in Unix time., defaults to None
        :type created_at: float, optional
        :param currency: The currency of the escrow balance. Three-letter ISO 4217 code., defaults to None
        :type currency: float, optional
        :param escrow_releases: Array of objects that describe individual releases., defaults to None
        :type escrow_releases: EscrowResponseEscrowReleases, optional
        :param id_: Indicates that the number of escrow releases is greater than the number returned in the response., defaults to None
        :type id_: str, optional
        :param last_payment_completion: Date and time of the completion of the last payment or partial payment, in Unix time., defaults to None
        :type last_payment_completion: float, optional
        :param payment: ID of the payment, a string starting with **payment_**., defaults to None
        :type payment: float, optional
        :param status: Status of the escrow. One of the following:<BR> * **pending** - The payment and escrow were created, but the payment is not completed and the funds are not in the escrow.<BR> * **on_hold** - The payment is completed and the funds are in escrow. canceled - The escrow is canceled.<BR>* **released** - All or part of the funds have been released to the wallets., defaults to None
        :type status: str, optional
        :param total_amount_released: Total amount of funds that were released to the wallets, in the currency defined in currency_code in the payment response., defaults to None
        :type total_amount_released: str, optional
        :param updated_at: Date and time of the last update to the escrow, in Unix time., defaults to None
        :type updated_at: float, optional
        """
        self.amount_on_hold = self._define_number(
            "amount_on_hold", amount_on_hold, nullable=True
        )
        self.created_at = self._define_number("created_at", created_at, nullable=True)
        self.currency = self._define_number("currency", currency, nullable=True)
        self.escrow_releases = self._define_object(
            escrow_releases, EscrowResponseEscrowReleases
        )
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.last_payment_completion = self._define_number(
            "last_payment_completion", last_payment_completion, nullable=True
        )
        self.payment = self._define_number("payment", payment, nullable=True)
        self.status = self._define_str("status", status, nullable=True)
        self.total_amount_released = self._define_str(
            "total_amount_released", total_amount_released, nullable=True
        )
        self.updated_at = self._define_number("updated_at", updated_at, nullable=True)
