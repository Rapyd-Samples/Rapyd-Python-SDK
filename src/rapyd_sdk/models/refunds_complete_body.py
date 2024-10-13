from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class RefundsCompleteBody(BaseModel):
    """RefundsCompleteBody

    :param token: ID of the refund. String starting with **refund_**.
    :type token: str
    """

    def __init__(self, token: str):
        """RefundsCompleteBody

        :param token: ID of the refund. String starting with **refund_**.
        :type token: str
        """
        self.token = token
