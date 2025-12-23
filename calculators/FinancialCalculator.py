from calculators import BasicCalculator

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
        return BasicCalculator.divide(annual_interest_rate, 12)

    @staticmethod
    def months_from_years(years: int) -> int:
        """
        Convert loan term in years to months.

        >>> FinancialCalculator.months_from_years(30)
        360
        """
        return BasicCalculator.multiply(years, 12)
