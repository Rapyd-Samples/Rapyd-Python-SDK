from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"type_": "type"})
class Limit(BaseModel):
    """Limit

    :param amount: The amount of the limit., defaults to None
    :type amount: float, optional
    :param currency: Three-letter ISO 4217 code for the currency of an existing account., defaults to None
    :type currency: str, optional
    :param type_: The limit type., defaults to None
    :type type_: str, optional
    :param updated_at: updated_at, defaults to None
    :type updated_at: int, optional
    """

    def __init__(
        self,
        amount: float = None,
        currency: str = None,
        type_: str = None,
        updated_at: int = None,
    ):
        """Limit

        :param amount: The amount of the limit., defaults to None
        :type amount: float, optional
        :param currency: Three-letter ISO 4217 code for the currency of an existing account., defaults to None
        :type currency: str, optional
        :param type_: The limit type., defaults to None
        :type type_: str, optional
        :param updated_at: updated_at, defaults to None
        :type updated_at: int, optional
        """
        self.amount = self._define_number("amount", amount, nullable=True)
        self.currency = self._define_str("currency", currency, nullable=True)
        self.type_ = self._define_str("type_", type_, nullable=True)
        self.updated_at = self._define_number("updated_at", updated_at, nullable=True)
