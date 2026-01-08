'''
Docstring for calculators.FinancialCalculator
'''

from .BasicCalculator import BasicCalculator


class FinancialCalculator(BasicCalculator):
    """
    Provides financial utility calculations based on BasicCalculator.

    This class converts annual rates and loan terms into
    monthly equivalents for use in mortgage calculations.
    """

    @staticmethod
    def calculate_monthly_interest_rate(annual_interest_rate: float) -> float:
        """
        Convert an annual interest rate to a monthly rate.

        Assumes the annual interest rate is expressed as a decimal
        (e.g., 0.06 for 6%).

        >>> FinancialCalculator.calculate_monthly_interest_rate(0.12)
        0.01
        """
        if annual_interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        return BasicCalculator.divide(annual_interest_rate, 12)

    @staticmethod
    def months_from_years(years: int) -> int:
        """
        Convert loan term in years to months.

        >>> FinancialCalculator.months_from_years(30)
        360
        """
        if years <= 0:
            raise ValueError("Loan term must be greater than zero.")
        return BasicCalculator.multiply(years, 12)


def calculate_monthly_interest_rate(annual_interest_rate: float) -> float:
    return FinancialCalculator.calculate_monthly_interest_rate(annual_interest_rate)


def months_from_years(years: int) -> int:
    return FinancialCalculator.months_from_years(years)


def multiply(x: float, y: float) -> float:
    return FinancialCalculator.multiply(x, y)


def divide(x: float, y: float) -> float:
    return FinancialCalculator.divide(x, y)
