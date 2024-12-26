from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from controllers.rating_controller import validate_payload, calculate_credit_rating_service

# Initialize Blueprint
api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/calculate_credit_rating", methods=["POST"])
def calculate_credit_rating():
    """Endpoint to calculate credit rating."""
    try:
        # Parse and validate payload
        payload = validate_payload(request.json)

        # Compute credit rating
        rating = calculate_credit_rating_service(payload.mortgages)
        response = {"status": "success", "credit_rating": rating}

        return jsonify(response), 200

    except ValidationError as e:
        # Handle validation errors
        return jsonify({"status": "error", "errors": e.errors()}), 400

    except Exception as e:
        # Log unexpected errors and return a generic message
        Logging.error(f"Unexpected Error: {str(e)}", exc_info=True)
        return jsonify({"status": "error", "message": "An unexpected error occurred."}), 500
