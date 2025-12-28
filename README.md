# PyBank Mortgage Engine
**PyBank Mortgage Engine** demonstrates how clean object-oriented design and financial domain modeling come together in Python.

## Architecture Overview

This project follows a **clean separation of concerns** between **domain models** (data) and **calculators** (business logic). The design emphasizes **immutability, stateless services, and extensibility**, mirroring real-world financial systems.

---

### Package Structure

```text
pybank/
|
|-- models/
|   |-- Loan (immutable dataclass)
|   |__ Borrower.py
│     
│
├── calculators/
│   |-- FinancialCalculator (stateless utilities)
│   │-- MortgageCalculator (domain-specific rules)
│   |__ AffordabilityCalculator
│ 
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
* **AffordabilityCalculator**: criteria based loan affordability 

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
      ↓
AffordabilityCalculator
```

New calculators (e.g., `RiskCalculator`) can be added without modifying existing code.

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

* Loan type factories (FHA, VA, Conventional)
* Scenario simulations
* REST or CLI interfaces

---


