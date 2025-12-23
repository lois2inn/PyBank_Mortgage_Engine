from dataclasses import dataclass

@dataclass(frozen=True)
class Loan:
    """
    Immutable data model representing a mortgage loan.
    """
    principal: float
    annual_interest_rate: float  # decimal, e.g. 0.06 for 6%
    years: int