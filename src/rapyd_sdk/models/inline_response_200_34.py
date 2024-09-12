from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status import Status
from .customer import Customer


@JsonMap({})
class InlineResponse200_34(BaseModel):
    """InlineResponse200_34

    :param status: status, defaults to None
    :type status: Status, optional
    :param data: customer, defaults to None
    :type data: Customer, optional
    """

    def __init__(self, status: Status = None, data: Customer = None):
        """InlineResponse200_34

        :param status: status, defaults to None
        :type status: Status, optional
        :param data: customer, defaults to None
        :type data: Customer, optional
        """
        self.status = self._define_object(status, Status)
        self.data = self._define_object(data, Customer)
