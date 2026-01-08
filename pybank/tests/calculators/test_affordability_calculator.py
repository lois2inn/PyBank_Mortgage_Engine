import pytest

from pybank.calculators.AffordabilityCalculator import AffordabilityCalculator
from pybank.models import Borrower


def test_max_monthly_housing_payment_standard():
    borrower = Borrower(
        monthly_income=6000,
        monthly_debt=500,
    )

    max_payment = AffordabilityCalculator.max_monthly_housing_payment(borrower)
    assert max_payment == 1660.00


def test_max_monthly_housing_payment_custom_dti():
    borrower = Borrower(
        monthly_income=8000,
        monthly_debt=1000,
    )

    max_payment = AffordabilityCalculator.max_monthly_housing_payment(
        borrower,
        max_dti=0.40,
    )
    assert max_payment == 2200.00


def test_max_monthly_housing_payment_invalid_income():
    borrower = Borrower(
        monthly_income=0,
        monthly_debt=500,
    )

    with pytest.raises(ValueError):
        AffordabilityCalculator.max_monthly_housing_payment(borrower)


def test_max_monthly_housing_payment_invalid_debt():
    borrower = Borrower(
        monthly_income=6000,
        monthly_debt=-1,
    )

    with pytest.raises(ValueError):
        AffordabilityCalculator.max_monthly_housing_payment(borrower)


def test_max_monthly_housing_payment_invalid_dti():
    borrower = Borrower(
        monthly_income=6000,
        monthly_debt=500,
    )

    with pytest.raises(ValueError):
        AffordabilityCalculator.max_monthly_housing_payment(borrower, max_dti=0)


def test_max_monthly_housing_payment_unaffordable():
    borrower = Borrower(
        monthly_income=1000,
        monthly_debt=400,
    )

    with pytest.raises(ValueError):
        AffordabilityCalculator.max_monthly_housing_payment(borrower, max_dti=0.36)


def test_max_loan_amount_standard():
    borrower = Borrower(
        monthly_income=6000,
        monthly_debt=500,
    )

    max_loan = AffordabilityCalculator.max_loan_amount(
        borrower,
        annual_interest_rate=0.06,
        years=30,
    )

    assert max_loan == 276874.08


def test_max_loan_amount_invalid_interest_rate():
    borrower = Borrower(
        monthly_income=6000,
        monthly_debt=500,
    )

    with pytest.raises(ValueError):
        AffordabilityCalculator.max_loan_amount(
            borrower,
            annual_interest_rate=-0.01,
            years=30,
        )


def test_max_loan_amount_invalid_years():
    borrower = Borrower(
        monthly_income=6000,
        monthly_debt=500,
    )

    with pytest.raises(ValueError):
        AffordabilityCalculator.max_loan_amount(
            borrower,
            annual_interest_rate=0.06,
            years=0,
        )
