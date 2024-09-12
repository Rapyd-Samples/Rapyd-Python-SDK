from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class HostedPageAdditionalResponseCartItems(BaseModel):
    """Describes the cart items that the customer is purchasing. These items are displayed at the checkout page.

    :param amount: The price of the item in the currency defined in currency., defaults to None
    :type amount: float, optional
    :param name: The name of the item., defaults to None
    :type name: str, optional
    :param quantity: The quantity of the item., defaults to None
    :type quantity: float, optional
    :param image: The image that appears in the checkout page for this item., defaults to None
    :type image: str, optional
    """

    def __init__(
        self,
        amount: float = None,
        name: str = None,
        quantity: float = None,
        image: str = None,
    ):
        """Describes the cart items that the customer is purchasing. These items are displayed at the checkout page.

        :param amount: The price of the item in the currency defined in currency., defaults to None
        :type amount: float, optional
        :param name: The name of the item., defaults to None
        :type name: str, optional
        :param quantity: The quantity of the item., defaults to None
        :type quantity: float, optional
        :param image: The image that appears in the checkout page for this item., defaults to None
        :type image: str, optional
        """
        self.amount = self._define_number("amount", amount, nullable=True)
        self.name = self._define_str("name", name, nullable=True)
        self.quantity = self._define_number("quantity", quantity, nullable=True)
        self.image = self._define_str("image", image, nullable=True)
