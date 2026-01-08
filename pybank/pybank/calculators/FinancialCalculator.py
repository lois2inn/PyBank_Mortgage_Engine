"""pybank.calculators.FinancialCalculator

This module provides small, stateless financial utility functions used by other
calculators (e.g., mortgage calculations).

The public API is available both as:

- Static methods on :class:`FinancialCalculator`
- Module-level wrapper functions for convenience

Examples:
    >>> from pybank.calculators.FinancialCalculator import (
    ...     calculate_monthly_interest_rate,
    ...     months_from_years,
    ... )
    >>> calculate_monthly_interest_rate(0.12)
    0.01
    >>> months_from_years(30)
    360
"""

from .BasicCalculator import BasicCalculator


class FinancialCalculator(BasicCalculator):
    """Stateless financial utility calculator.

    This class converts annual rates and loan terms into monthly equivalents for
    use in mortgage calculations.
    """

    @staticmethod
    def calculate_monthly_interest_rate(annual_interest_rate: float) -> float:
        """Convert an annual interest rate to a monthly interest rate.

        Args:
            annual_interest_rate: Annual interest rate expressed as a decimal
                (e.g., `0.06` for 6%).

        Returns:
            The monthly interest rate expressed as a decimal.

        Raises:
            ValueError: If `annual_interest_rate` is negative.

        Examples:
            >>> from pybank.calculators.FinancialCalculator import FinancialCalculator
            >>> FinancialCalculator.calculate_monthly_interest_rate(0.12)
            0.01
        """
        if annual_interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        return BasicCalculator.divide(annual_interest_rate, 12)

    @staticmethod
    def months_from_years(years: int) -> int:
        """Convert a loan term from years to months.

        Args:
            years: Loan term in years.

        Returns:
            Loan term in months.

        Raises:
            ValueError: If `years` is not greater than zero.

        Examples:
            >>> from pybank.calculators.FinancialCalculator import FinancialCalculator
            >>> FinancialCalculator.months_from_years(30)
            360
        """
        if years <= 0:
            raise ValueError("Loan term must be greater than zero.")
        return BasicCalculator.multiply(years, 12)


def calculate_monthly_interest_rate(annual_interest_rate: float) -> float:
    """Convenience wrapper for :meth:`FinancialCalculator.calculate_monthly_interest_rate`.

    Args:
        annual_interest_rate: Annual interest rate expressed as a decimal.

    Returns:
        The monthly interest rate.

    Examples:
        >>> from pybank.calculators.FinancialCalculator import calculate_monthly_interest_rate
        >>> calculate_monthly_interest_rate(0.12)
        0.01
    """
    return FinancialCalculator.calculate_monthly_interest_rate(annual_interest_rate)


def months_from_years(years: int) -> int:
    """Convenience wrapper for :meth:`FinancialCalculator.months_from_years`.

    Args:
        years: Loan term in years.

    Returns:
        Loan term in months.

    Examples:
        >>> from pybank.calculators.FinancialCalculator import months_from_years
        >>> months_from_years(30)
        360
    """
    return FinancialCalculator.months_from_years(years)


def multiply(x: float, y: float) -> float:
    """Convenience wrapper for :meth:`BasicCalculator.multiply`.

    Args:
        x: First operand.
        y: Second operand.

    Returns:
        The product of `x` and `y`.

    Examples:
        >>> from pybank.calculators.FinancialCalculator import multiply
        >>> multiply(6, 7)
        42
    """
    return FinancialCalculator.multiply(x, y)


def divide(x: float, y: float) -> float:
    """Convenience wrapper for :meth:`BasicCalculator.divide`.

    Args:
        x: Numerator.
        y: Denominator.

    Returns:
        The quotient `x / y`.

    Raises:
        ValueError: If `y` is zero.

    Examples:
        >>> from pybank.calculators.FinancialCalculator import divide
        >>> divide(10, 2)
        5.0
    """
    return FinancialCalculator.divide(x, y)
