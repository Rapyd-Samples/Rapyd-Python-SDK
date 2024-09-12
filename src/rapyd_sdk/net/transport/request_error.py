from .response import Response
from typing import Optional


class RequestError(IOError):
    """
    Class representing a Request Error.

    :ivar bool is_http_error: Indicates if the error is an HTTP error.
    :ivar int status: The status code of the HTTP error.
    :ivar Optional[Response] response: The response associated with the error.
    """

    def __init__(
        self,
        message: str,
        status: Optional[int] = None,
        response: Optional[Response] = None,
        stack: Optional["RequestError"] = None,
    ):
        """
        Initialize a new instance of RequestError.

        :param str message: The error message.
        :param Optional[int] status: The status code of the HTTP error.
        :param Optional[Response] response: The response associated with the error.
        """
        super().__init__(message)
        self.response = response
        self.stack = stack

        if status is not None:
            self.status = status
            self.is_http_error = True
        else:
            self.status = -1
            self.is_http_error = False

    def __str__(self):
        """
        Get the string representation of the error.

        :return: The string representation of the error.
        :rtype: str
        """
        error_stack = []
        current_error = self
        while current_error is not None:
            error_stack.append(
                f"Error: {super().__str__()}, Status Code: {current_error.status}"
            )
            current_error = current_error.stack
        return "\n".join(error_stack)
