from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class Status(BaseModel):
    """Status

    :param error_code: Error code of the API request., defaults to None
    :type error_code: str, optional
    :param message: Description about the API., defaults to None
    :type message: str, optional
    :param operation_id: Unique identifier to track the request., defaults to None
    :type operation_id: str, optional
    :param response_code: Response code of the API., defaults to None
    :type response_code: str, optional
    :param status: Status of the api indicating success or failure., defaults to None
    :type status: str, optional
    """

    def __init__(
        self,
        error_code: str = None,
        message: str = None,
        operation_id: str = None,
        response_code: str = None,
        status: str = None,
    ):
        """Status

        :param error_code: Error code of the API request., defaults to None
        :type error_code: str, optional
        :param message: Description about the API., defaults to None
        :type message: str, optional
        :param operation_id: Unique identifier to track the request., defaults to None
        :type operation_id: str, optional
        :param response_code: Response code of the API., defaults to None
        :type response_code: str, optional
        :param status: Status of the api indicating success or failure., defaults to None
        :type status: str, optional
        """
        self.error_code = self._define_str("error_code", error_code, nullable=True)
        self.message = self._define_str("message", message, nullable=True)
        self.operation_id = self._define_str(
            "operation_id", operation_id, nullable=True
        )
        self.response_code = self._define_str(
            "response_code", response_code, nullable=True
        )
        self.status = self._define_str("status", status, nullable=True)
