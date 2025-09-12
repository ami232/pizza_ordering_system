from pizza import PizzaFactory, ItalianPizzaFactory, AmericanPizzaFactory
from order import OrderManager

factory = PizzaFactory()
manager = OrderManager()

# Factory Method
pizza = factory.create_margherita()
manager.add_order([pizza])
manager.list_orders()
manager.prepare_order(1)

# Abstract Factory
italian_factory = ItalianPizzaFactory()
american_factory = AmericanPizzaFactory()

italian_pizza = italian_factory.create_margherita()
american_pizza = american_factory.create_margherita()

manager.add_order([italian_pizza])
manager.add_order([american_pizza])
manager.list_orders()

# Step 1
margherita_pizza = italian_factory.create_margherita()
pepperoni_pizza = italian_factory.create_pepperoni()
veggie_pizza = italian_factory.create_custom("Veggie", ["tomato sauce", "mozzarella", "onion", "mushrooms"])

manager.add_order([margherita_pizza])
manager.add_order([pepperoni_pizza])
manager.add_order([veggie_pizza])

manager.list_orders()

# Step 2
hawaiian_pizza = italian_factory.create_hawaiian()
hawaiian_pizza.prepare()
