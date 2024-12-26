from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from models.schemas import RMBSPayload
from core.credit_rating import CreditRatingService
from utils.logger import logger

# Initialize Blueprint
api = Blueprint("api", __name__, url_prefix="/api")


def validate_payload(data):
    """Validate and parse the incoming payload."""
    try:
        return RMBSPayload.parse_obj(data)
    except ValidationError as e:
        logger.error(f"Validation Error: {e.json()}")
        raise


@api.route("/calculate_credit_rating", methods=["POST"])
def calculate_credit_rating():
    """Endpoint to calculate credit rating."""
    try:
        # Parse and validate payload
        payload = validate_payload(request.json)

        # Compute credit rating
        rating = CreditRatingService().calculate_credit_rating(payload.mortgages)
        response = {"status": "success", "credit_rating": rating}

        return jsonify(response), 200

    except ValidationError as e:
        # Handle validation errors
        return jsonify({"status": "error", "errors": e.errors()}), 400

    except Exception as e:
        # Log unexpected errors and return a generic message
        logger.error(f"Unexpected Error: {str(e)}", exc_info=True)
        return jsonify({"status": "error", "message": "An unexpected error occurred."}), 500
