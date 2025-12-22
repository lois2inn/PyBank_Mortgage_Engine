# PyBank_Mortgage_Engine
**PyBank Mortgage Engine** demonstrates how clean object-oriented design and financial domain modeling come together in Python.

## Architecture Overview

This project follows a **clean separation of concerns** between **domain models** (data) and **calculators** (business logic). The design emphasizes **immutability, stateless services, and extensibility**, mirroring real-world financial systems.

---

### High-Level Architecture

```text
+--------------------+        +-----------------------------+
|   Domain Models    |        |         Calculators         |
|--------------------|        |-----------------------------|
| Loan (@dataclass)  | -----> | FinancialCalculator         |
|                    |        |  - interest conversions     |
|  (data only)       |        |  - time conversions         |
+--------------------+        |  - basic math utilities     |
                              |             ^               |
                              |             |               |
                              |   MortgageCalculator         |
                              |  - monthly payment           |
                              |  - loan amount               |
                              |  - validation rules          |
                              +-----------------------------+
```

---

### Package Structure

```text
pybank-mortgage-engine/
│
├── models/
│   └── loan.py
│       └── Loan (immutable dataclass)
│
├── calculators/
│   ├── financial.py
│   │   └── FinancialCalculator (stateless utilities)
│   └── mortgage.py
│       └── MortgageCalculator (domain-specific rules)
│
├── tests/
│   ├── test_financial_calculator.py
│   └── test_mortgage_calculator.py
│
├── README.md
├── pyproject.toml / setup.cfg
└── requirements.txt
```

---

## Design Principles Applied

### 1. Single Responsibility Principle (SRP)

* **Loan**: stores loan data only
* **FinancialCalculator**: generic financial math
* **MortgageCalculator**: mortgage-specific formulas

### 2. Stateless Calculators

* Calculators do not store data
* All inputs are passed explicitly
* Safe for reuse, testing, and concurrency

### 3. Immutable Domain Models

* Models use `@dataclass(frozen=True)`
* Prevents accidental mutation
* Encourages predictable behavior

### 4. Extensibility by Inheritance

```text
BasicCalculator
      ↓
FinancialCalculator
      ↓
MortgageCalculator
```

New calculators (e.g., `AffordabilityCalculator`, `RiskCalculator`) can be added without modifying existing code.

---

## Example Data Flow

```text
Loan (model)
   ↓
MortgageCalculator.monthly_payment(loan)
   ↓
FinancialCalculator utilities
   ↓
Monthly payment result
```

---

## Future Extensions

* Borrower model (income, debts)
* AffordabilityCalculator (DTI rules)
* Loan type factories (FHA, VA, Conventional)
* Scenario simulations
* REST or CLI interfaces

---


