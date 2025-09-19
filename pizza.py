from abc import ABC, abstractmethod
from typing import List


class Pizza:
    """
    Represents a pizza with a name, list of ingredients, and preparation status.
    """

    def __init__(self, name: str, ingredients: List[str]):
     
        self.name = name
        self.ingredients = ingredients
        self.prepared = False

    def prepare(self):
        """
        Prepares the pizza if it has not been prepared yet.
        """
        if not self.prepared:
            print(f"Preparing {self.name} pizza...")
            print("Ingredients:", ", ".join(self.ingredients))
            print("Baking in the oven... Done!")
            self.prepared = True
        else:
            print(f"{self.name} pizza is already prepared!")

    def __str__(self):
        return f"{self.name} ({', '.join(self.ingredients)}) - {'Prepared' if self.prepared else 'Not Prepared'}"


# Factory
class PizzaFactory:
    """
    Factory class responsible for creating Pizza objects based on the specified type.
    """

    def create_custom(self, name, ingredients):
        return Pizza(name, ingredients)

    def create_margherita(self):
        return Pizza("Margherita", ["tomato sauce", "mozzarella", "basil"])

    def create_pepperoni(self):
        return Pizza("Pepperoni", ["tomato sauce", "mozzarella", "pepperoni"])
    
    def create_hawaiian(self):
        return Pizza("Hawaiian", ["tomato sauce", "mozzarella", "pepperoni", "pineapple"])

# Abstract Factory
class PizzaFactoryAbstract(ABC):
    def create_custom(self, name, ingredients) -> Pizza:
        return Pizza(name, ingredients)

    @abstractmethod
    def create_margherita(self) -> Pizza:
        pass

    @abstractmethod
    def create_pepperoni(self) -> Pizza:
        pass


# Concrete Factories
class ItalianPizzaFactory(PizzaFactoryAbstract):

    def create_margherita(self):
        return Pizza("Italian Margherita", ["tomato sauce", "mozzarella", "basil"])

    def create_pepperoni(self):
        return Pizza("Italian Pepperoni", ["tomato sauce", "mozzarella", "pepperoni"])


class AmericanPizzaFactory(PizzaFactoryAbstract):
    def create_margherita(self):
        return Pizza("American Margherita", ["tomato sauce", "mozzarella", "oregano"])

    def create_pepperoni(self):
        return Pizza(
            "American Pepperoni",
            ["tomato sauce", "mozzarella", "pepperoni", "extra cheese"],
        )
