from pydantic import ValidationError
from domain.credit_rating import CreditRatingService
from schemas.rmbs import RMBSPayload
from utils.logger import Logging


def validate_payload(data):
    """Validate and parse the incoming payload."""
    try:
        return RMBSPayload.parse_obj(data)
    except ValidationError as e:
        Logging.error(f"Validation Error: {e.json()}")
        raise


def calculate_credit_rating_service(mortgages):
    """Service to calculate credit rating."""
    return CreditRatingService().calculate_credit_rating(mortgages)
