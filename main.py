from pizza import *
from order import *

factory = PizzaFactory()
manager = OrderManager()

margherita = factory.create_margherita()
pepperoni = factory.create_pepperoni()
veggie = factory.create_veggie()
manager.add_order([margherita])
manager.add_order([pepperoni])
manager.add_order([veggie])
manager.list_orders()

hawaiian = factory.create_hawaiian()
hawaiian_order = manager.add_order([hawaiian])
print("Added Hawaiian pizza:")
manager.list_orders()
print("Preparing Hawaiian pizza order:")
manager.prepare_order(hawaiian_order.order_id)
manager.list_orders()


italian_factory = ItalianPizzaFactory()
american_factory = AmericanPizzaFactory()

italian_pizza = italian_factory.create_margherita()
american_pizza = american_factory.create_margherita()

manager.add_order([italian_pizza])
manager.add_order([american_pizza])
print("\nOrders after adding Italian and American Margherita:")
manager.list_orders()