from typing import Any, Dict
from pydantic import ValidationError
from configs.constants import (
    VALIDATION_ERROR_MSG,
    ERROR_CALCULATING_RATING_MSG
)
from domain.credit_rating import CreditRatingService
from schemas.rmbs import RMBSPayload
from utils.logger import project_logger


def validate_payload(data: Dict[str, Any]) -> RMBSPayload:
    """
    Validate and parse the incoming payload.

    Args:
        data (Dict[str, Any]): The incoming data, expected to match the structure of RMBSPayload.

    Returns:
        RMBSPayload: Parsed payload if valid.

    Raises:
        ValidationError: If the payload is not valid according to the RMBSPayload schema.
    """
    try:
        return RMBSPayload.parse_obj(data)
    except ValidationError as e:
        project_logger.error(f"{VALIDATION_ERROR_MSG}: {e.json()}")
        raise ValidationError(f"Validation failed: {e}") from e


def calculate_credit_rating_service(mortgages: Dict[str, Any]) -> float:
    """
    Service to calculate credit rating based on mortgage data.

    Args:
        mortgages (Dict[str, Any]): The mortgage data, expected to be a dictionary containing mortgage details.

    Returns:
        float: The calculated credit rating based on the mortgage data.

    Raises:
        Exception: If there is any error during the credit rating calculation process.
    """
    try:
        return CreditRatingService().calculate_credit_rating(mortgages)
    except Exception as e:
        project_logger.error(f"{ERROR_CALCULATING_RATING_MSG}: {e}")
        raise Exception(ERROR_CALCULATING_RATING_MSG) from e
