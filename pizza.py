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
