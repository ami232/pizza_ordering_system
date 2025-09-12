class Pizza:
    """
    Represents a pizza with a name, list of ingredients, and preparation status.
    """

    def __init__(self, name, ingredients):
        """
        Initializes a Pizza instance.

        Parameters:
            name (str): The name of the pizza.
            ingredients (list of str): List of ingredients for the pizza.
        """
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


class PizzaFactory:
    """
    Factory class responsible for creating Pizza objects based on the specified type.
    """

    @staticmethod
    def create_pizza(pizza_type):
        """
        Creates a Pizza object based on the specified type.

        Parameters:
            pizza_type (str): The type of pizza to create (e.g., "margherita", "pepperoni").

        Returns:
            Pizza: An instance of the Pizza class corresponding to the specified type.

        Raises:
            ValueError: If the pizza_type is unknown.
        """
        if pizza_type == "margherita":
            return Pizza("Margherita", ["tomato sauce", "mozzarella", "basil"])
        elif pizza_type == "pepperoni":
            return Pizza("Pepperoni", ["tomato sauce", "mozzarella", "pepperoni"])
        else:
            raise ValueError(f"Unknown pizza type '{pizza_type}'")
