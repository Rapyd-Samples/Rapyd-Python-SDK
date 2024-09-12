from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class TransferResponseBody(BaseModel):
    """TransferResponseBody

    :param id_: ID of the transfer transaction, from the `id` field in the `data` object of the response. 32-digit hexadecimal.
    :type id_: str
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param status: Determines how to handle the transfer. One of the following values - accept, decline, cancel
    :type status: str
    """

    def __init__(self, id_: str, status: str, metadata: dict = None):
        """TransferResponseBody

        :param id_: ID of the transfer transaction, from the `id` field in the `data` object of the response. 32-digit hexadecimal.
        :type id_: str
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param status: Determines how to handle the transfer. One of the following values - accept, decline, cancel
        :type status: str
        """
        self.id_ = id_
        self.metadata = metadata
        self.status = status
