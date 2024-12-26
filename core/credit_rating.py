from abc import ABC, abstractmethod


class RiskScoreCalculator(ABC):
    @abstractmethod
    def calculate(self, mortgage):
        pass


class LoanToValueRisk(RiskScoreCalculator):
    def calculate(self, mortgage):
        ltv = mortgage.loan_amount / mortgage.property_value
        if ltv > 0.9:
            return 2
        elif ltv > 0.8:
            return 1
        return 0


class DebtToIncomeRisk(RiskScoreCalculator):
    def calculate(self, mortgage):
        dti = (mortgage.debt_amount / mortgage.annual_income) * 100
        if dti > 50:
            return 2
        elif dti > 40:
            return 1
        return 0


class CreditScoreRisk(RiskScoreCalculator):
    def calculate(self, mortgage):
        if mortgage.credit_score >= 700:
            return -1
        elif mortgage.credit_score < 650:
            return 1
        return 0


class LoanTypeRisk(RiskScoreCalculator):
    def calculate(self, mortgage):
        return -1 if mortgage.loan_type == "fixed" else 1


class PropertyTypeRisk(RiskScoreCalculator):
    def calculate(self, mortgage):
        return 1 if mortgage.property_type == "condo" else 0


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
        if avg_credit_score >= 700:
            total_score -= 1
        elif avg_credit_score < 650:
            total_score += 1

        if total_score <= 2:
            return "AAA"
        elif total_score <= 5:
            return "BBB"
        return "C"
