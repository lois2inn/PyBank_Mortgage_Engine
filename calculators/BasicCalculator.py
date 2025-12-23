class BasicCalculator:
    """
    A basic calculator providing fundamental arithmetic operations.

    This class serves as the base class for more advanced financial
    and mortgage calculators.
    """

    @staticmethod
    def multiply(x: float, y: float) -> float:
        """
        Multiply two numbers.

        >>> BasicCalculator.multiply(3, 4)
        12
        """
        return x * y

    @staticmethod
    def divide(x: float, y: float) -> float:
        """
        Divide x by y.

        >>> BasicCalculator.divide(10, 2)
        5.0

        >>> BasicCalculator.divide(5, 0)
        Traceback (most recent call last):
        ...
        ValueError: Cannot divide by zero.
        """
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y