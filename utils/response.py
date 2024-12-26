from http import HTTPStatus
from typing import Optional, Dict, Any
from flask import jsonify
from utils.logger import project_logger
from configs.constants import DEFAULT_ERROR_MESSAGE, ERROR_MSG_LOGGING_EXCEPTION, DEFAULT_MSG, STATUS_CODE, DATA, MSG, \
    EMPTY_DATA


class ApiResponse:
    def __init__(self, msg: Optional[str] = None, status_code: Optional[int] = None, data: Optional[Dict[str, Any]] = None):
        """
        Initialize an API response object with a message, status code, and optional data.

        Args:
            msg (Optional[str]): The response message.
            status_code (Optional[int]): The HTTP status code (default is HTTPStatus.OK).
            data (Optional[Dict[str, Any]]): The response data (default is None).
        """
        self.msg = msg
        self.status_code = status_code or HTTPStatus.OK  # Default to HTTP 200
        self.data = data

    def set_response(self, msg: str, status_code: int, data: Optional[Dict[str, Any]] = None) -> None:
        """
        Set the response message, status code, and data.

        Args:
            msg (str): The response message.
            status_code (int): The HTTP status code.
            data (Optional[Dict[str, Any]]): Additional response data (default is None).
        """
        self.msg = msg
        self.status_code = status_code
        self.data = data

    def result(self) -> Dict[str, Any]:
        """
        Return the response as a dictionary.

        Returns:
            Dict[str, Any]: The API response data in dictionary form.
        """
        return {
            MSG: self.msg if self.msg is not None else DEFAULT_MSG,
            STATUS_CODE: self.status_code.value,  # Get the numerical value of the status code
            DATA: self.data if self.data is not None else EMPTY_DATA
        }


def create_api_response(
    msg: str,
    status_code: int,
    data: Optional[Dict[str, Any]] = None
) -> Any:
    """
    Utility function to create a consistent API response.

    Args:
        msg (str): The response message.
        status_code (int): HTTP status code.
        data (Optional[Dict[str, Any]]): Additional response data (default: None).

    Returns:
        Any: Flask JSON response object.
    """
    try:
        response = ApiResponse()
        response.set_response(msg=msg, status_code=status_code, data=data)
        return jsonify(response.result())
    except Exception as e:
        project_logger.error(f"Error in creating API response: {e}")
        return create_api_response(msg=DEFAULT_ERROR_MESSAGE, status_code=HTTPStatus.INTERNAL_SERVER_ERROR)


def handle_error(
    exception: Exception,
    message: str,
    status_code: int,
    log_message: Optional[str] = None
) -> Any:
    """
    Helper function to handle error responses and log the exception.

    Args:
        exception (Exception): The exception raised.
        message (str): The response message.
        status_code (int): The HTTP status code.
        log_message (Optional[str]): The log message to be recorded (default: None).

    Returns:
        Any: Flask JSON response object for the error.
    """
    try:
        if log_message:
            project_logger.error(f"{log_message}: {exception}")
        return create_api_response(msg=message, status_code=status_code, data={})
    except Exception as e:
        project_logger.error(f"{ERROR_MSG_LOGGING_EXCEPTION}: {e}")
        return create_api_response(msg=DEFAULT_ERROR_MESSAGE, status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
