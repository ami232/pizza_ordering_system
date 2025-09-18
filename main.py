from pizza import PizzaFactory, ItalianPizzaFactory, AmericanPizzaFactory, JapanesePizzaFactory
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
japanese_factory = JapanesePizzaFactory()

italian_pizza = italian_factory.create_margherita()
american_pizza = american_factory.create_margherita()
japanese_pizza = japanese_factory.create_pepperoni()

italian_order = manager.add_order([italian_pizza])
american_order = manager.add_order([american_pizza])
japanese_order = manager.add_order([japanese_pizza])

print("Before prepare")
manager.list_orders()
manager.prepare_order(italian_order.order_id)
manager.prepare_order(american_order.order_id)
manager.prepare_order(japanese_order.order_id)


print("After prepare")
manager.list_orders()

manager.dispatch_order(japanese_order.order_id)
print("After dispatch")
manager.list_orders()
