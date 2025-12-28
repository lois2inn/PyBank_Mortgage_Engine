from calculators import MortgageCalculator
from models import Borrower

class AffordabilityCalculator:
    """
    Determines loan affordability based on income, debt,
    and standard DTI (Debt-to-Income) rules.
    """
    DEFAULT_MAX_DTI = 0.36  # 36%

    @staticmethod
    def max_monthly_housing_payment(
        borrower: Borrower,
        max_dti: float = DEFAULT_MAX_DTI
    ) -> float:
        """
        Calculate the maximum affordable monthly housing payment.

        >>> borrower = Borrower(monthly_income=6000, monthly_debt=500)
        >>> AffordabilityCalculator.max_monthly_housing_payment(borrower)
        1660.0
        """
        AffordabilityCalculator._validate_borrower(borrower)

        if not 0 < max_dti <= 1:
            raise ValueError("DTI must be between 0 and 1.")

        max_total_debt = borrower.monthly_income * max_dti
        max_housing_payment = max_total_debt - borrower.monthly_debt

        if max_housing_payment <= 0:
            raise ValueError("Borrower cannot afford additional housing payment.")

        return round(max_housing_payment, 2)

    @staticmethod
    def max_loan_amount(
        borrower: Borrower,
        annual_interest_rate: float,
        years: int,
        max_dti: float = DEFAULT_MAX_DTI
    ) -> float:
        """
        Calculate the maximum loan amount a borrower can afford.

        >>> borrower = Borrower(monthly_income=6000, monthly_debt=500)
        >>> round(AffordabilityCalculator.max_loan_amount(borrower, 0.06, 30), 2)
        276500.00
        """
        max_payment = AffordabilityCalculator.max_monthly_housing_payment(
            borrower, max_dti
        )

        return MortgageCalculator.loan_amount(
            monthly_payment=max_payment,
            annual_interest_rate=annual_interest_rate,
            years=years
        )

    @staticmethod
    def _validate_borrower(borrower: Borrower) -> None:
        """
        Validate borrower inputs.
        """
        if borrower.monthly_income <= 0:
            raise ValueError("Monthly income must be greater than zero.")
        if borrower.monthly_debt < 0:
            raise ValueError("Monthly debt cannot be negative.")