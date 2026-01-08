import pytest
from pybank.models import Loan
from pybank.calculators.MortgageCalculator import monthly_payment,loan_amount


def test_monthly_payment_standard_loan():
    loan = Loan(
        principal=300_000,
        annual_interest_rate=0.06,
        years=30
    )

    payment = monthly_payment(loan)
    assert payment == 1798.65


def test_monthly_payment_zero_interest():
    loan = Loan(
        principal=120_000,
        annual_interest_rate=0.0,
        years=10
    )

    payment = monthly_payment(loan)
    assert payment == 1000.00


def test_monthly_payment_invalid_principal():
    loan = Loan(
        principal=0,
        annual_interest_rate=0.05,
        years=30
    )

    with pytest.raises(ValueError):
        monthly_payment(loan)


def test_monthly_payment_invalid_years():
    loan = Loan(
        principal=200_000,
        annual_interest_rate=0.05,
        years=0
    )

    with pytest.raises(ValueError):
        monthly_payment(loan)


def test_loan_amount_standard():
    computed_loan_amount = loan_amount(
        monthly_payment=1800,
        annual_interest_rate=0.06,
        years=30
    )

    assert round(computed_loan_amount, 2) == 300224.91


def test_loan_amount_zero_interest():
    computed_loan_amount = loan_amount(
        monthly_payment=1000,
        annual_interest_rate=0.0,
        years=10
    )

    assert computed_loan_amount == 120000


def test_loan_amount_invalid_payment():
    with pytest.raises(ValueError):
        loan_amount(
            monthly_payment=0,
            annual_interest_rate=0.05,
            years=30
        )


def test_loan_amount_invalid_interest_rate():
    with pytest.raises(ValueError):
        loan_amount(
            monthly_payment=1500,
            annual_interest_rate=-0.01,
            years=30
        )


def test_loan_amount_invalid_years():
    with pytest.raises(ValueError):
        loan_amount(
            monthly_payment=1500,
            annual_interest_rate=0.05,
            years=0
        )