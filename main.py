from pizza import PizzaFactory, ItalianPizzaFactory, AmericanPizzaFactory
from order import OrderManager

factory = PizzaFactory()
manager = OrderManager()

# Factory Method
pizza = factory.create_margherita()
hawaiian = factory.create_hawaiian()  # Step 2
manager.add_order([pizza])
manager.add_order([hawaiian])         # add Hawaiian as a separate order

# Show initial state
manager.list_orders()

# Step 3: prepare the first order and show that it changed to Prepared
manager.prepare_order(1)
manager.list_orders()

# Abstract Factory
italian_factory = ItalianPizzaFactory()
american_factory = AmericanPizzaFactory()

italian_pizza = italian_factory.create_margherita()
american_pizza = american_factory.create_margherita()

manager.add_order([italian_pizza])
manager.add_order([american_pizza])
manager.list_orders()
