from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .contact import Contact
from .status import Status


@JsonMap({})
class InlineResponse200_2(BaseModel):
    """InlineResponse200_2

    :param data: data, defaults to None
    :type data: Contact, optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: Contact = None, status: Status = None):
        """InlineResponse200_2

        :param data: data, defaults to None
        :type data: Contact, optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_object(data, Contact)
        self.status = self._define_object(status, Status)
