from typing import Any
from flask import Blueprint, request
from controllers.rating_controller import validate_payload, calculate_credit_rating_service
from utils.response import create_api_response, handle_error
from utils.decorators import log_method
from utils.logger import project_logger
from configs.constants import (
    API_BLUEPRINT_NAME,
    API_URL_PREFIX,
    CREDIT_RATING_ENDPOINT,
    SUCCESS_MSG,
    ERROR_MSG,
    CREDIT_RATING_NOT_FOUND_MSG,
    CREDIT_RATING,
    UNEXPECTED_ERROR,
    VALIDATION_ERROR_MSG,
    INPUT_ERROR_MSG,
    MISSING_KEY_IN_PAYLOAD_MSG,
    INCORRECT_TYPE_IN_PAYLOAD_MSG,
)
from http import HTTPStatus
from json import JSONDecodeError

# Initialize Blueprint
api = Blueprint(API_BLUEPRINT_NAME, __name__, url_prefix=API_URL_PREFIX)


@api.route(CREDIT_RATING_ENDPOINT, methods=["POST"])
@log_method
def calculate_credit_rating() -> Any:
    """
    Endpoint to calculate credit rating.

    Returns:
        Any: JSON response object with the result or error details.
    """
    try:
        # Parse and validate payload
        payload = validate_payload(request.json)

        # Compute credit rating
        rating = calculate_credit_rating_service(payload.mortgages)

        if not rating:
            project_logger.warning(CREDIT_RATING_NOT_FOUND_MSG)
            return create_api_response(
                msg=CREDIT_RATING_NOT_FOUND_MSG,
                status_code=HTTPStatus.NOT_FOUND,
                data={},
            )

        return create_api_response(
            msg=SUCCESS_MSG,
            status_code=HTTPStatus.OK,
            data={CREDIT_RATING: rating},
        )

    except JSONDecodeError as e:
        return handle_error(e, INPUT_ERROR_MSG, HTTPStatus.BAD_REQUEST, "Invalid JSON format")
    except ValueError as e:
        return handle_error(e, VALIDATION_ERROR_MSG, HTTPStatus.UNPROCESSABLE_ENTITY, "Validation failed")
    except KeyError as e:
        return handle_error(e, MISSING_KEY_IN_PAYLOAD_MSG, HTTPStatus.BAD_REQUEST, "Missing key in payload")
    except TypeError as e:
        return handle_error(e, INCORRECT_TYPE_IN_PAYLOAD_MSG, HTTPStatus.BAD_REQUEST, "Incorrect type in payload")
    except Exception as e:
        return handle_error(e, ERROR_MSG, HTTPStatus.INTERNAL_SERVER_ERROR, UNEXPECTED_ERROR)
