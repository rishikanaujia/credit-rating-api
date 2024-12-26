from flask import Blueprint, request, jsonify
from controllers.rating_controller import validate_payload, calculate_credit_rating_service
from utils.api_response import ApiResponse
from utils.decorators import log_method
from utils.logger import project_logger
from http import HTTPStatus
from typing import Any, Dict, Optional

# Initialize Blueprint
api = Blueprint("api", __name__, url_prefix="/api")


@log_method
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



@api.route("/calculate_credit_rating", methods=["POST"])
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
            # If no valid rating is found, raise a 404 Not Found error
            project_logger.warning("Credit rating not found for the given input.")

        # Return success response with the computed credit rating
        return create_api_response(
            msg="Credit rating calculation successful",
            status_code=HTTPStatus.OK,
            data={"credit_rating": rating}
        )

    # except ValidationError as e:
    #     return create_api_response(
    #         msg="Invalid input",
    #         status_code=HTTPStatus.BAD_REQUEST,
    #         data={"errors": e.errors()}
    #     )
    #
    # except NotFound as e:
    #
    #     return create_api_response(
    #         msg="Resource not found",
    #         status_code=HTTPStatus.NOT_FOUND,
    #         data={"error": str(e.description)}
    #     )

    except Exception as e:
        return create_api_response(
            msg="An unexpected error occurred.",
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            data={}
        )
