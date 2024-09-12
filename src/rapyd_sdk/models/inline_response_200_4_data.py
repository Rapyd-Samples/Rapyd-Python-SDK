from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .inline_response_200_4_data_compliance_levels import (
    InlineResponse200_4DataComplianceLevels,
)


@JsonMap({})
class InlineResponse200_4Data(BaseModel):
    """InlineResponse200_4Data

    :param compliance_levels: compliance_levels, defaults to None
    :type compliance_levels: List[InlineResponse200_4DataComplianceLevels], optional
    """

    def __init__(
        self, compliance_levels: List[InlineResponse200_4DataComplianceLevels] = None
    ):
        """InlineResponse200_4Data

        :param compliance_levels: compliance_levels, defaults to None
        :type compliance_levels: List[InlineResponse200_4DataComplianceLevels], optional
        """
        self.compliance_levels = self._define_list(
            compliance_levels, InlineResponse200_4DataComplianceLevels
        )
