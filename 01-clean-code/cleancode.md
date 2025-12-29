# Object-Oriented Programming and Clean Code

## Why OOP Matters
Object-Oriented Programming models software as interacting objects, each combining data and behavior. This alignment with real-world concepts promotes modularity, encapsulation, and reuse.

### Core Pillars
- **Encapsulation**: Group data with the methods that operate on it, exposing only what is necessary.
- **Abstraction**: Provide clear interfaces while hiding implementation details.
- **Inheritance**: Reuse shared behavior by deriving specialized classes from a base.
- **Polymorphism**: Interchange objects through shared interfaces to reduce branching logic.

```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        ...

class CreditCard(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Charged ${amount:.2f} to credit card.")

class DigitalWallet(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Processed ${amount:.2f} via digital wallet.")

def checkout(amount: float, method: PaymentMethod) -> None:
    method.pay(amount)

checkout(42.0, CreditCard())
checkout(42.0, DigitalWallet())
```

## Practicing Clean Code
- **Clarity over cleverness**: Choose explicit names, consistent casing, and small functions.
- **Single responsibility**: Each module, class, or function should do one thing well.
- **Meaningful comments**: Explain _why_ when the intent is not obvious; avoid narrating the code.
- **Consistent formatting**: Follow a style guide (e.g., PEP 8) to reduce cognitive overhead during reviews.

## Embracing DRY (Don’t Repeat Yourself)
- Extract common logic into reusable functions, classes, or templates.
- Prefer configuration over duplication when behavior varies slightly.
- Automate repetitive tasks with scripts or build tools.
- Regularly refactor to eliminate newly introduced repetition.

## Putting It Together
1. Model the domain with cohesive classes.
2. Express intent with clean naming and minimal indentation depth.
3. Consolidate shared behavior to keep abstractions lean.
4. Continuously refactor as the codebase evolves to maintain readability and adaptability.

**What is OOP?**

Object-Oriented Programming, or "OOP", is a pattern or paradigm for (allegedly) organizing(writing) code to make more readable, maintainable, in effect for writing clean code.

**What is clean code?**

Code that's easily readable and maintainable for other programmers. It does not affect performance, it more stylistic way of writing code to make it more easier to maintain when the inevitable future updates come about.

## Clean Code helps with:
- readability: makes your code more readable for other programmers.
- proceess speeds: makes the development process faster
- fixes: it is easier to find and squash bugs

## D.R.Y. Code - DO NOT REPEAT YOURSELF:
Avoid copying blocks of logic in multiple places; instead, centralize it in well-named utilities or classes so fixes happen once.  
- Introduce abstractions only when duplication is real, not hypothetical.  
- Prefer composition or configuration files when behavior varies slightly.  
- Use tests and linters to catch regressions when refactoring shared code paths.  
- Schedule periodic reviews to identify fresh duplication before it hardens.  