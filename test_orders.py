from pizza import PizzaFactory
from order import OrderManager

factory = PizzaFactory()
manager = OrderManager()

# Factory Method
pizza1 = factory.create_margherita()
pizza2 = factory.create_pepperoni()
pizza3 = factory.create_custom("Veggie", ["tomato sauce", "mozzarella", "bell peppers", "onions", "olives"])

manager.add_order([pizza1, pizza2, pizza3])
manager.list_orders()