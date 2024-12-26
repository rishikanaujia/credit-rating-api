from http import HTTPStatus
from typing import Optional, Dict, Any

from flask import jsonify
from utils.logger import project_logger


class ApiResponse:
    def __init__(self, msg=None, status_code=None, data=None):
        self.msg = msg
        self.status_code = status_code or HTTPStatus.OK  # Default to HTTP 200
        self.data = data

    def set_response(self, msg, status_code, data):
        self.msg = msg
        self.status_code = status_code
        self.data = data

    def result(self):
        return {
            'msg': self.msg if self.msg is not None else 'No message provided',
            'status_code': self.status_code.value,  # Get the numerical value of the status code
            'data': self.data if self.data is not None else {}
        }


def create_api_response(msg: str, status_code: int, data: Optional[Dict[str, Any]] = None) -> Any:
    """
    Utility function to create a consistent API response.

    Args:
        msg (str): Response message.
        status_code (int): HTTP status code.
        data (Optional[Dict[str, Any]]): Additional response data (default: None).

    Returns:
        Any: Flask JSON response object.
    """
    response = ApiResponse()
    response.set_response(msg=msg, status_code=status_code, data=data)
    return jsonify(response.result())


def handle_error(exception: Exception, message: str, status_code: int, log_message: Optional[str] = None) -> Any:
    """
    Helper function to handle error responses.

    Args:
        exception (Exception): The exception raised.
        message (str): The response message.
        status_code (int): The HTTP status code.
        log_message (Optional[str]): The log message (default: None).

    Returns:
        Any: Flask JSON response object.
    """
    if log_message:
        project_logger.error(f"{log_message}: {exception}")
    return create_api_response(msg=message, status_code=status_code, data={})
