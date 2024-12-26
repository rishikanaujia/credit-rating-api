from http import HTTPStatus


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
