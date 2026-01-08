import pytest
from pybank.calculators.FinancialCalculator import months_from_years, calculate_monthly_interest_rate, multiply, divide


def test_calculate_monthly_interest_rate():
    assert calculate_monthly_interest_rate(0.12) == 0.01


def test_calculate_monthly_interest_rate_zero():
    assert calculate_monthly_interest_rate(0.0) == 0.0


def test_calculate_monthly_interest_rate_negative():
    with pytest.raises(ValueError):
        calculate_monthly_interest_rate(-0.05)


def test_months_from_years():
    assert months_from_years(30) == 360


def test_months_from_years_invalid():
    with pytest.raises(ValueError):
        months_from_years(0)


def test_multiply():
    assert multiply(6, 7) == 42


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)