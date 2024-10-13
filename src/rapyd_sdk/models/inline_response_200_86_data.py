from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"type_": "type"})
class InlineResponse200_86Data(BaseModel):
    """InlineResponse200_86Data

    :param country: The two-letter ISO 3166-1 ALPHA-2 code for the country of the identification document., defaults to None
    :type country: str, optional
    :param type_: Type of the identification document. Two-letter code, defaults to None
    :type type_: str, optional
    :param name: Name of the identification document. Two-letter code, defaults to None
    :type name: str, optional
    :param is_back_required: Boolean if back image required, defaults to None
    :type is_back_required: bool, optional
    :param is_address_extractable: Boolean if address extractable, defaults to None
    :type is_address_extractable: bool, optional
    """

    def __init__(
        self,
        country: str = None,
        type_: str = None,
        name: str = None,
        is_back_required: bool = None,
        is_address_extractable: bool = None,
    ):
        """InlineResponse200_86Data

        :param country: The two-letter ISO 3166-1 ALPHA-2 code for the country of the identification document., defaults to None
        :type country: str, optional
        :param type_: Type of the identification document. Two-letter code, defaults to None
        :type type_: str, optional
        :param name: Name of the identification document. Two-letter code, defaults to None
        :type name: str, optional
        :param is_back_required: Boolean if back image required, defaults to None
        :type is_back_required: bool, optional
        :param is_address_extractable: Boolean if address extractable, defaults to None
        :type is_address_extractable: bool, optional
        """
        self.country = self._define_str("country", country, nullable=True)
        self.type_ = self._define_str("type_", type_, nullable=True)
        self.name = self._define_str("name", name, nullable=True)
        self.is_back_required = is_back_required
        self.is_address_extractable = is_address_extractable
