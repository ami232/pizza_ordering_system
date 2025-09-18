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

from pizza import BeaPizzaFactory

bea_factory = BeaPizzaFactory()
bea_marg = bea_factory.create_margherita()
bea_truffle = bea_factory.create_truffle_queen()

manager.add_order([bea_marg, bea_truffle])
manager.list_orders()
manager.prepare_order(3)     # adjust ID if needed
manager.dispatch_order(3)    # optional bonus