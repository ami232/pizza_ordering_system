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
        if not self.prepared:
            print(f"Preparing {self.name} pizza...")
            print("Ingredients:", ", ".join(self.ingredients))
            print("Baking in the oven... Done!")
            self.prepared = True
        else:
            print(f"{self.name} pizza is already prepared!")

    def __str__(self):
        return f"{self.name} ({', '.join(self.ingredients)}) - {'Prepared' if self.prepared else 'Not Prepared'}"


# ------------------ Simple Factory ------------------
class PizzaFactory:
    def create_custom(self, name: str, ingredients: List[str]) -> Pizza:
        return Pizza(name, ingredients)

    def create_margherita(self) -> Pizza:
        return Pizza("Margherita", ["tomato sauce", "mozzarella", "basil"])

    def create_pepperoni(self) -> Pizza:
        return Pizza("Pepperoni", ["tomato sauce", "mozzarella", "pepperoni"])

    def create_veggie(self) -> Pizza:
        return Pizza("Veggie", ["tomato sauce", "mozzarella", "peppers", "onions", "olives"])

    def create_hawaiian(self) -> Pizza:
        return Pizza("Hawaiian", ["tomato sauce", "mozzarella", "ham", "pineapple"])


# ------------------ Abstract Factory ------------------
class PizzaFactoryAbstract(ABC):
    def create_custom(self, name: str, ingredients: List[str]) -> Pizza:
        return Pizza(name, ingredients)

    @abstractmethod
    def create_margherita(self) -> Pizza:
        pass

    @abstractmethod
    def create_pepperoni(self) -> Pizza:
        pass

    @abstractmethod
    def create_veggie(self) -> Pizza:
        pass

    @abstractmethod
    def create_hawaiian(self) -> Pizza:
        pass


# ------------------ Concrete Factories ------------------
class ItalianPizzaFactory(PizzaFactoryAbstract):
    def create_margherita(self) -> Pizza:
        return Pizza("Italian Margherita", ["tomato sauce", "mozzarella", "basil"])

    def create_pepperoni(self) -> Pizza:
        return Pizza("Italian Pepperoni", ["tomato sauce", "mozzarella", "pepperoni"])

    def create_veggie(self) -> Pizza:
        return Pizza("Italian Veggie", ["tomato sauce", "mozzarella", "zucchini", "peppers", "onions"])

    def create_hawaiian(self) -> Pizza:
        return Pizza("Italian Hawaiian", ["tomato sauce", "mozzarella", "ham", "pineapple"])


class AmericanPizzaFactory(PizzaFactoryAbstract):
    def create_margherita(self) -> Pizza:
        return Pizza("American Margherita", ["tomato sauce", "mozzarella", "oregano"])

    def create_pepperoni(self) -> Pizza:
        return Pizza("American Pepperoni", ["tomato sauce", "mozzarella", "pepperoni", "extra cheese"])

    def create_veggie(self) -> Pizza:
        return Pizza("American Veggie", ["tomato sauce", "mozzarella", "mushrooms", "peppers", "onions", "olives"])

    def create_hawaiian(self) -> Pizza:
        return Pizza("American Hawaiian", ["tomato sauce", "mozzarella", "ham", "pineapple", "extra cheese"])


class MiaPizzaFactory(PizzaFactoryAbstract):
    def create_margherita(self) -> Pizza:
        return Pizza("Mia Margherita", ["tomato sauce", "mozzarella", "basil", "oregano"])

    def create_pepperoni(self) -> Pizza:
        return Pizza("Mia Pepperoni", ["tomato sauce", "mozzarella", "pepperoni", "jalapenos"])

    def create_veggie(self) -> Pizza:
        return Pizza("Mia Veggie", ["tomato sauce", "mozzarella", "peppers", "onions", "corn"])

    def create_hawaiian(self) -> Pizza:
        return Pizza("Mia Hawaiian", ["tomato sauce", "mozzarella", "ham", "pineapple", "bacon"])

    def create_bbq(self) -> Pizza:  # New pizza unique to your factory
        return Pizza("Mia BBQ", ["bbq sauce", "mozzarella", "chicken", "onions"])

