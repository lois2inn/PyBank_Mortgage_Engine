from dataclasses import dataclass

@dataclass(frozen=True)
class Borrower:
    """
    Represents a loan applicant.
    """
    monthly_income: float
    monthly_debt: float  # existing debt obligations