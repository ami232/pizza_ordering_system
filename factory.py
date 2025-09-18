# factory.py
from abc import ABC, abstractmethod
from pizza import Pizza

class PizzaFactoryAbstract(ABC):
    @abstractmethod
    def create_pizza(self, kind: str) -> Pizza:
        """Return a Pizza instance of the requested kind."""
        pass

class AdriPizzaFactory(PizzaFactoryAbstract):
    MENU = {
        "margherita": ["tomato", "mozzarella", "basil"],
        "pepperoni":  ["tomato", "mozzarella", "pepperoni"],
        # NEW TYPE you’re adding for Step 4:
        "bbq_chicken": ["bbq sauce", "mozzarella", "chicken", "red onion"],
    }

    def create_pizza(self, kind: str) -> Pizza:
        kind = kind.lower()
        if kind not in self.MENU:
            raise ValueError(f"Unknown pizza type: {kind}")
        return Pizza(kind.title(), self.MENU[kind])
