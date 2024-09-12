from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class InlineResponse200_4DataElements(BaseModel):
    """InlineResponse200_4DataElements

    :param element_name: element_name, defaults to None
    :type element_name: str, optional
    :param verified: verified, defaults to None
    :type verified: bool, optional
    """

    def __init__(self, element_name: str = None, verified: bool = None):
        """InlineResponse200_4DataElements

        :param element_name: element_name, defaults to None
        :type element_name: str, optional
        :param verified: verified, defaults to None
        :type verified: bool, optional
        """
        self.element_name = self._define_str(
            "element_name", element_name, nullable=True
        )
        self.verified = verified
