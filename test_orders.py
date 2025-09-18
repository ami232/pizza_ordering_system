from pizza import PizzaFactory, ItalianPizzaFactory, AmericanPizzaFactory, PizzaFactoryAbstract, Pizza
from order import OrderManager

factory = PizzaFactory()
manager = OrderManager()

# Factory Method
pizza1 = factory.create_margherita()
pizza2 = factory.create_pepperoni()
pizza3 = factory.create_custom("Veggie", ["tomato sauce", "mozzarella", "bell peppers", "onions", "olives"])
pizza4 = factory.create_hawaiian()

manager.add_order([pizza1, pizza2, pizza3])
manager.add_order([pizza4])
manager.list_orders()

# Abstract Factory Example
italian_factory = ItalianPizzaFactory()
american_factory = AmericanPizzaFactory()

italian_pizza = italian_factory.create_margherita()
american_pizza = american_factory.create_margherita()

manager.add_order([italian_pizza])
manager.add_order([american_pizza])
manager.list_orders()

# Bonus: Your own factory
class SofiaPizzaFactory(PizzaFactoryAbstract):
    def create_margherita(self):
        return Pizza("Sofia Margherita", ["tomato sauce", "mozzarella", "basil", "oregano"])
    def create_pepperoni(self):
        return Pizza("Sofia Pepperoni", ["tomato sauce", "mozzarella", "pepperoni", "jalapenos"])
    def create_special(self):
        return Pizza("Sofia Special", ["pesto sauce", "goat cheese", "sun-dried tomatoes"])

sofia_factory = SofiaPizzaFactory()
special_pizza = sofia_factory.create_special()
manager.add_order([special_pizza])
manager.list_orders()

# Prepare orders
manager.prepare_order(1)
manager.list_orders()