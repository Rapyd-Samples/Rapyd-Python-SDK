from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class ApplePayObject(BaseModel):
    """ApplePayObject

    :param display_name: The canonical name for the client's business, suitable for display. 64 or fewer UTF-8 characters. Relevant to Apple Pay.
    :type display_name: str
    :param initiative_context: The client's fully qualified domain name, without the final period. For example, **acmegeneralproducts.rapyd.net**
    :type initiative_context: str
    """

    def __init__(self, display_name: str, initiative_context: str):
        """ApplePayObject

        :param display_name: The canonical name for the client's business, suitable for display. 64 or fewer UTF-8 characters. Relevant to Apple Pay.
        :type display_name: str
        :param initiative_context: The client's fully qualified domain name, without the final period. For example, **acmegeneralproducts.rapyd.net**
        :type initiative_context: str
        """
        self.display_name = display_name
        self.initiative_context = initiative_context
