"""pybank.calculators.MortgageCalculator

Mortgage-specific calculations such as computing a fixed monthly payment and
deriving a loan principal from an affordable monthly payment.

The public API is available both as:

- Static methods on :class:`MortgageCalculator`
- Module-level wrapper functions for convenience

Examples:
    >>> from pybank.models import Loan
    >>> from pybank.calculators.MortgageCalculator import monthly_payment, loan_amount
    >>> monthly_payment(Loan(principal=300_000, annual_interest_rate=0.06, years=30))
    1798.65
    >>> loan_amount(monthly_payment=1800, annual_interest_rate=0.06, years=30)
    300224.91
"""

from .FinancialCalculator import FinancialCalculator
from ..models import Loan


class MortgageCalculator(FinancialCalculator):
    """Stateless mortgage calculator.

    This class performs mortgage-specific calculations and contains no state.
    All methods operate purely on inputs.
    """

    @staticmethod
    def monthly_payment(loan: Loan) -> float:
        """Calculate the fixed monthly mortgage payment.

        Args:
            loan: Loan model containing principal, annual interest rate (decimal)
                and term in years.

        Returns:
            Monthly payment rounded to 2 decimals.

        Raises:
            ValueError: If loan principal is not greater than zero.
            ValueError: If loan term is not greater than zero.
            ValueError: If interest rate is negative.

        Examples:
            >>> from pybank.models import Loan
            >>> from pybank.calculators.MortgageCalculator import MortgageCalculator
            >>> MortgageCalculator.monthly_payment(
            ...     Loan(principal=300_000, annual_interest_rate=0.06, years=30)
            ... )
            1798.65
            >>> MortgageCalculator.monthly_payment(
            ...     Loan(principal=120_000, annual_interest_rate=0.0, years=10)
            ... )
            1000.0
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
        """Calculate the loan principal implied by a monthly payment.

        Args:
            monthly_payment: Monthly payment amount.
            annual_interest_rate: Annual interest rate expressed as a decimal.
            years: Loan term in years.

        Returns:
            Loan amount (principal) rounded to 2 decimals.

        Raises:
            ValueError: If `monthly_payment` is not greater than zero.
            ValueError: If `annual_interest_rate` is negative.
            ValueError: If `years` is not greater than zero.

        Examples:
            >>> from pybank.calculators.MortgageCalculator import MortgageCalculator
            >>> MortgageCalculator.loan_amount(1800, 0.06, 30)
            300224.91
            >>> MortgageCalculator.loan_amount(1000, 0.0, 10)
            120000.0
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


def monthly_payment(loan: Loan) -> float:
    """Convenience wrapper for :meth:`MortgageCalculator.monthly_payment`.

    Args:
        loan: Loan model containing principal, annual interest rate, and term.

    Returns:
        Monthly payment rounded to 2 decimals.

    Examples:
        >>> from pybank.models import Loan
        >>> from pybank.calculators.MortgageCalculator import monthly_payment
        >>> monthly_payment(Loan(principal=300_000, annual_interest_rate=0.06, years=30))
        1798.65
    """
    return MortgageCalculator.monthly_payment(loan)


def loan_amount(monthly_payment: float, annual_interest_rate: float, years: int) -> float:
    """Convenience wrapper for :meth:`MortgageCalculator.loan_amount`.

    Args:
        monthly_payment: Monthly payment amount.
        annual_interest_rate: Annual interest rate expressed as a decimal.
        years: Loan term in years.

    Returns:
        Loan amount (principal) rounded to 2 decimals.

    Examples:
        >>> from pybank.calculators.MortgageCalculator import loan_amount
        >>> loan_amount(monthly_payment=1800, annual_interest_rate=0.06, years=30)
        300224.91
    """
    return MortgageCalculator.loan_amount(
        monthly_payment=monthly_payment,
        annual_interest_rate=annual_interest_rate,
        years=years,
    )
