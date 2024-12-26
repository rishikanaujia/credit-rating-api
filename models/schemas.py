from pydantic import BaseModel, Field, PositiveFloat
from typing import List, Literal

class Mortgage(BaseModel):
    credit_score: int = Field(..., ge=300, le=850, description="Borrower's credit score")
    loan_amount: PositiveFloat
    property_value: PositiveFloat
    annual_income: PositiveFloat
    debt_amount: PositiveFloat
    loan_type: Literal["fixed", "adjustable"]
    property_type: Literal["single_family", "condo"]

class RMBSPayload(BaseModel):
    mortgages: List[Mortgage]
