from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .beneficiary import Beneficiary


@JsonMap({})
class InlineResponse200_14Data(BaseModel):
    """InlineResponse200_14Data

    :param beneficiary: beneficiary, defaults to None
    :type beneficiary: Beneficiary, optional
    :param validated: validation status, defaults to None
    :type validated: bool, optional
    """

    def __init__(self, beneficiary: Beneficiary = None, validated: bool = None):
        """InlineResponse200_14Data

        :param beneficiary: beneficiary, defaults to None
        :type beneficiary: Beneficiary, optional
        :param validated: validation status, defaults to None
        :type validated: bool, optional
        """
        self.beneficiary = self._define_object(beneficiary, Beneficiary)
        self.validated = validated
