from calculators import FinancialCalculator
from models import Loan

class MortgageCalculator(FinancialCalculator):
    """
    Performs mortgage-specific calculations such as monthly payments
    and loan amount estimation using Loan model
    This class contains no state and operates entirely on input models.
    """

    @staticmethod
    def monthly_payment(loan: Loan) -> float:
        """
        Calculate the fixed monthly mortgage payment.

        >>> loan = Loan(300000, 0.06, 30)
        >>> MortgageCalculator.monthly_payment(loan)
        1798.65
        """
        MortgageCalculator._validate_loan(loan)

        monthly_rate = FinancialCalculator.calculate_monthly_interest_rate(
            loan.annual_interest_rate
        )
        months = FinancialCalculator.months_from_years(loan.years)

        # Zero-interest loan edge case
        if monthly_rate == 0:
            return round(loan.principal / months, 2)

        numerator = monthly_rate * (1 + monthly_rate) ** months
        denominator = (1 + monthly_rate) ** months - 1

        multiplier = FinancialCalculator.divide(numerator, denominator)
        return round(loan.principal * multiplier, 2)

    @staticmethod
    def loan_amount(
        monthly_payment: float,
        annual_interest_rate: float,
        years: int
    ) -> float:
        """
        Calculate the loan amount based on payment, interest rate, and term.

        >>> MortgageCalculator.loan_amount(1800, 0.06, 30)
        300229.29
        """
        if monthly_payment <= 0:
            raise ValueError("Monthly payment must be greater than zero.")
        if annual_interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if years <= 0:
            raise ValueError("Loan term must be greater than zero.")

        monthly_rate = FinancialCalculator.calculate_monthly_interest_rate(
            annual_interest_rate
        )
        months = FinancialCalculator.months_from_years(years)

        # Zero-interest loan edge case
        if monthly_rate == 0:
            return round(monthly_payment * months, 2)

        return round(
            (
                monthly_payment
                * ((1 + monthly_rate) ** months - 1)
                / (monthly_rate * (1 + monthly_rate) ** months)
            ),
            2,
        )

    @staticmethod
    def _validate_loan(loan: Loan) -> None:
        """
        Validate loan attributes before calculation.
        """
        if loan.principal <= 0:
            raise ValueError("Loan principal must be greater than zero.")
        if loan.annual_interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if loan.years <= 0:
            raise ValueError("Loan term must be greater than zero.")