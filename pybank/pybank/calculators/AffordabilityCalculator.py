"""pybank.calculators.AffordabilityCalculator

Affordability calculations based on Debt-to-Income (DTI) constraints.

This module provides utilities to:

- Compute the maximum affordable monthly housing payment, given borrower income
  and existing monthly debt.
- Convert that affordable payment into a maximum loan amount using the mortgage
  amortization formula.

The public API is available both as:

- Static methods on :class:`AffordabilityCalculator`
- Module-level wrapper functions for convenience

Examples:
    >>> from pybank.models import Borrower
    >>> from pybank.calculators.AffordabilityCalculator import (
    ...     max_monthly_housing_payment,
    ...     max_loan_amount,
    ... )
    >>> borrower = Borrower(monthly_income=6000, monthly_debt=500)
    >>> max_monthly_housing_payment(borrower)
    1660.0
    >>> max_loan_amount(borrower, annual_interest_rate=0.06, years=30)
    276874.08
"""

from .MortgageCalculator import MortgageCalculator
from ..models import Borrower


class AffordabilityCalculator:
    """Stateless affordability calculator based on DTI rules.

    Attributes:
        DEFAULT_MAX_DTI: Default maximum debt-to-income ratio, expressed as a
            decimal (e.g., `0.36` for 36%).
    """
    DEFAULT_MAX_DTI = 0.36  # 36%

    @staticmethod
    def max_monthly_housing_payment(
        borrower: Borrower,
        max_dti: float = DEFAULT_MAX_DTI
    ) -> float:
        """Calculate the maximum affordable monthly housing payment.

        This uses the standard DTI approach:

        `max_housing = (monthly_income * max_dti) - monthly_debt`

        Args:
            borrower: Borrower model containing `monthly_income` and
                `monthly_debt`.
            max_dti: Maximum debt-to-income ratio as a decimal in `(0, 1]`.

        Returns:
            Maximum affordable monthly housing payment, rounded to 2 decimals.

        Raises:
            ValueError: If borrower income is not greater than zero.
            ValueError: If borrower monthly debt is negative.
            ValueError: If `max_dti` is not in `(0, 1]`.
            ValueError: If the computed housing payment is not positive.

        Examples:
            >>> from pybank.models import Borrower
            >>> from pybank.calculators.AffordabilityCalculator import AffordabilityCalculator
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
            raise ValueError(
                "Borrower cannot afford additional housing payment.")

        return round(max_housing_payment, 2)

    @staticmethod
    def max_loan_amount(
        borrower: Borrower,
        annual_interest_rate: float,
        years: int,
        max_dti: float = DEFAULT_MAX_DTI
    ) -> float:
        """Calculate the maximum loan amount a borrower can afford.

        This first calculates the maximum affordable monthly housing payment
        using :meth:`max_monthly_housing_payment`, then converts that payment to
        a loan amount using :meth:`pybank.calculators.MortgageCalculator.MortgageCalculator.loan_amount`.

        Args:
            borrower: Borrower model.
            annual_interest_rate: Annual interest rate as a decimal.
            years: Loan term in years.
            max_dti: Maximum debt-to-income ratio as a decimal.

        Returns:
            Maximum loan amount (principal) rounded to 2 decimals.

        Raises:
            ValueError: Propagated from :meth:`max_monthly_housing_payment`.
            ValueError: If `annual_interest_rate` is negative.
            ValueError: If `years` is not greater than zero.

        Examples:
            >>> from pybank.models import Borrower
            >>> from pybank.calculators.AffordabilityCalculator import AffordabilityCalculator
            >>> borrower = Borrower(monthly_income=6000, monthly_debt=500)
            >>> AffordabilityCalculator.max_loan_amount(borrower, 0.06, 30)
            276874.08
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


def max_monthly_housing_payment(
    borrower: Borrower,
    max_dti: float = AffordabilityCalculator.DEFAULT_MAX_DTI,
) -> float:
    """Convenience wrapper for :meth:`AffordabilityCalculator.max_monthly_housing_payment`.

    Args:
        borrower: Borrower model.
        max_dti: Maximum debt-to-income ratio as a decimal.

    Returns:
        Maximum affordable monthly housing payment rounded to 2 decimals.

    Examples:
        >>> from pybank.models import Borrower
        >>> from pybank.calculators.AffordabilityCalculator import max_monthly_housing_payment
        >>> max_monthly_housing_payment(Borrower(monthly_income=6000, monthly_debt=500))
        1660.0
    """
    return AffordabilityCalculator.max_monthly_housing_payment(borrower, max_dti)


def max_loan_amount(
    borrower: Borrower,
    annual_interest_rate: float,
    years: int,
    max_dti: float = AffordabilityCalculator.DEFAULT_MAX_DTI,
) -> float:
    """Convenience wrapper for :meth:`AffordabilityCalculator.max_loan_amount`.

    Args:
        borrower: Borrower model.
        annual_interest_rate: Annual interest rate as a decimal.
        years: Loan term in years.
        max_dti: Maximum debt-to-income ratio as a decimal.

    Returns:
        Maximum loan amount (principal) rounded to 2 decimals.

    Examples:
        >>> from pybank.models import Borrower
        >>> from pybank.calculators.AffordabilityCalculator import max_loan_amount
        >>> borrower = Borrower(monthly_income=6000, monthly_debt=500)
        >>> max_loan_amount(borrower, annual_interest_rate=0.06, years=30)
        276874.08
    """
    return AffordabilityCalculator.max_loan_amount(
        borrower=borrower,
        annual_interest_rate=annual_interest_rate,
        years=years,
        max_dti=max_dti,
    )
