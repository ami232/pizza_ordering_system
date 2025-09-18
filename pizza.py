from abc import ABC, abstractmethod

class Pizza:
    """
    Represents a pizza with a name, list of ingredients, and preparation status.
    """

    def __init__(self, name, ingredients):
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


# ------------------ Factory ------------------
class PizzaFactory:
    def create_custom(self, name, ingredients):
        return Pizza(name, ingredients)

    def create_margherita(self):
        return Pizza("Margherita", ["tomato sauce", "mozzarella", "basil"])

    def create_pepperoni(self):
        return Pizza("Pepperoni", ["tomato sauce", "mozzarella", "pepperoni"])

    def create_veggie(self):
        return Pizza("Veggie", ["tomato sauce", "mozzarella", "peppers", "onions", "olives"])

    def create_hawaiian(self):
        return Pizza("Hawaiian", ["tomato sauce", "mozzarella", "ham", "pineapple"])



# ------------------ Abstract Factory ------------------
class PizzaFactoryAbstract(ABC):
    def create_custom(self, name, ingredients) -> Pizza:
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
    def create_margherita(self):
        return Pizza("Italian Margherita", ["tomato sauce", "mozzarella", "basil"])

    def create_pepperoni(self):
        return Pizza("Italian Pepperoni", ["tomato sauce", "mozzarella", "pepperoni"])

    def create_veggie(self):
        return Pizza("Italian Veggie", ["tomato sauce", "mozzarella", "zucchini", "peppers", "onions"])

    def create_hawaiian(self):
        return Pizza("Italian Hawaiian", ["tomato sauce", "mozzarella", "ham", "pineapple"])


class AmericanPizzaFactory(PizzaFactoryAbstract):
    def create_margherita(self):
        return Pizza("American Margherita", ["tomato sauce", "mozzarella", "oregano"])

    def create_pepperoni(self):
        return Pizza("American Pepperoni", ["tomato sauce", "mozzarella", "pepperoni", "extra cheese"])

    def create_veggie(self):
        return Pizza("American Veggie", ["tomato sauce", "mozzarella", "mushrooms", "peppers", "onions", "olives"])

    def create_hawaiian(self):
        return Pizza("American Hawaiian", ["tomato sauce", "mozzarella", "ham", "pineapple", "extra cheese"])

class ManuelPizzaFactory(PizzaFactoryAbstract):
    def create_margherita(self):
        return Pizza("Manuel Margherita", ["tomato sauce", "mozzarella", "spinach"])

    def create_pepperoni(self):
        return Pizza("Manuel Pepperoni", ["tomato sauce", "mozzarella", "pepperoni", "jalapeños"])

    def create_veggie(self):
        return Pizza("Manuel Veggie", ["tomato sauce", "mozzarella", "peppers", "onions", "corn"])

    def create_hawaiian(self):
        return Pizza("Manuel Hawaiian", ["tomato sauce", "mozzarella", "ham", "pineapple", "bacon"])

    def create_bbq(self):
        return Pizza("Manuel BBQ", ["bbq sauce", "mozzarella", "chicken", "onions"])
