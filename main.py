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
from pizza import PizzaFactory, ItalianPizzaFactory, AmericanPizzaFactory
from order import OrderManager

# Singleton
manager = OrderManager()
factory = PizzaFactory()

# Step 1 - Place Orders
order1 = manager.add_order([factory.create_margherita(), factory.create_pepperoni()])
order2 = manager.add_order([factory.create_hawaiian()])

manager.list_orders()

# Step 3 - Prepare Orders
manager.prepare_order(1)
manager.list_orders()

# Step 3 - Dispatch Orders
manager.dispatch_order(1)
manager.list_orders()

# Step 4 - Abstract Factory
italian_factory = ItalianPizzaFactory()
american_factory = AmericanPizzaFactory()

order3 = manager.add_order([italian_factory.create_margherita()])
order4 = manager.add_order([american_factory.create_pepperoni()])

manager.list_orders()
manager.prepare_order(3)
manager.prepare_order(4)
manager.dispatch_order(3)
manager.list_orders()
