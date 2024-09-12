from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class RefundsRefundIdBody(BaseModel):
    """RefundsRefundIdBody

    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: any, optional
    """

    def __init__(self, metadata: any = None):
        """RefundsRefundIdBody

        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: any, optional
        """
        self.metadata = metadata
