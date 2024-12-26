from abc import ABC, abstractmethod
from utils.decorators import log_method
from configs.constants import (
    LTV_HIGH_THRESHOLD, LTV_MEDIUM_THRESHOLD, LTV_HIGH_SCORE, LTV_MEDIUM_SCORE, LTV_LOW_SCORE,
    DTI_HIGH_THRESHOLD, DTI_MEDIUM_THRESHOLD, DTI_HIGH_SCORE, DTI_MEDIUM_SCORE, DTI_LOW_SCORE,
    CREDIT_SCORE_GOOD, CREDIT_SCORE_POOR, CREDIT_SCORE_GOOD_DEDUCTION, CREDIT_SCORE_POOR_ADDITION, CREDIT_SCORE_NEUTRAL,
    LOAN_TYPE_FIXED, LOAN_TYPE_ADJUSTABLE, LOAN_TYPE_FIXED_SCORE, LOAN_TYPE_ADJUSTABLE_SCORE,
    PROPERTY_TYPE_SINGLE_FAMILY, PROPERTY_TYPE_CONDO, PROPERTY_TYPE_SINGLE_FAMILY_SCORE, PROPERTY_TYPE_CONDO_SCORE,
    RATING_SCORE_AAA, RATING_SCORE_BBB, RATING_AAA, RATING_BBB, RATING_C
)


class RiskScoreCalculator(ABC):
    @abstractmethod
    def calculate(self, mortgage):
        pass


class LoanToValueRisk(RiskScoreCalculator):
    @log_method
    def calculate(self, mortgage):
        ltv = mortgage.loan_amount / mortgage.property_value
        if ltv > LTV_HIGH_THRESHOLD:
            return LTV_HIGH_SCORE
        elif ltv > LTV_MEDIUM_THRESHOLD:
            return LTV_MEDIUM_SCORE
        return LTV_LOW_SCORE


class DebtToIncomeRisk(RiskScoreCalculator):
    @log_method
    def calculate(self, mortgage):
        dti = (mortgage.debt_amount / mortgage.annual_income) * 100
        if dti > DTI_HIGH_THRESHOLD:
            return DTI_HIGH_SCORE
        elif dti > DTI_MEDIUM_THRESHOLD:
            return DTI_MEDIUM_SCORE
        return DTI_LOW_SCORE


class CreditScoreRisk(RiskScoreCalculator):
    def calculate(self, mortgage):
        if mortgage.credit_score >= CREDIT_SCORE_GOOD:
            return CREDIT_SCORE_GOOD_DEDUCTION
        elif mortgage.credit_score < CREDIT_SCORE_POOR:
            return CREDIT_SCORE_POOR_ADDITION
        return CREDIT_SCORE_NEUTRAL


class LoanTypeRisk(RiskScoreCalculator):
    def calculate(self, mortgage):
        if mortgage.loan_type == LOAN_TYPE_FIXED:
            return LOAN_TYPE_FIXED_SCORE
        elif mortgage.loan_type == LOAN_TYPE_ADJUSTABLE:
            return LOAN_TYPE_ADJUSTABLE_SCORE
        return 0  # Fallback for unexpected loan types


class PropertyTypeRisk(RiskScoreCalculator):
    def calculate(self, mortgage):
        if mortgage.property_type == PROPERTY_TYPE_CONDO:
            return PROPERTY_TYPE_CONDO_SCORE
        elif mortgage.property_type == PROPERTY_TYPE_SINGLE_FAMILY:
            return PROPERTY_TYPE_SINGLE_FAMILY_SCORE
        return 0  # Fallback for unexpected property types


class CreditRatingService:
    def __init__(self):
        self.risk_calculators = [
            LoanToValueRisk(),
            DebtToIncomeRisk(),
            CreditScoreRisk(),
            LoanTypeRisk(),
            PropertyTypeRisk()
        ]

    def calculate_risk_score(self, mortgage):
        return sum(calculator.calculate(mortgage) for calculator in self.risk_calculators)

    def calculate_credit_rating(self, mortgages):
        total_score = sum(self.calculate_risk_score(m) for m in mortgages)

        avg_credit_score = sum(m.credit_score for m in mortgages) / len(mortgages)
        if avg_credit_score >= CREDIT_SCORE_GOOD:
            total_score -= 1
        elif avg_credit_score < CREDIT_SCORE_POOR:
            total_score += 1

        if total_score <= RATING_SCORE_AAA:
            return RATING_AAA
        elif total_score <= RATING_SCORE_BBB:
            return RATING_BBB
        return RATING_C
