from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class InlineResponse200_90DataApplicationType(BaseModel):
    """InlineResponse200_90DataApplicationType

    :param application_type: application_type, defaults to None
    :type application_type: str, optional
    :param entity_type: entity_type, defaults to None
    :type entity_type: str, optional
    :param country: country, defaults to None
    :type country: str, optional
    """

    def __init__(
        self, application_type: str = None, entity_type: str = None, country: str = None
    ):
        """InlineResponse200_90DataApplicationType

        :param application_type: application_type, defaults to None
        :type application_type: str, optional
        :param entity_type: entity_type, defaults to None
        :type entity_type: str, optional
        :param country: country, defaults to None
        :type country: str, optional
        """
        self.application_type = self._define_str(
            "application_type", application_type, nullable=True
        )
        self.entity_type = self._define_str("entity_type", entity_type, nullable=True)
        self.country = self._define_str("country", country, nullable=True)
