
from pizza import PizzaFactory
from order import OrderManager

factory = PizzaFactory()
manager = OrderManager()


hawaiian_pizza = factory.create_hawaiian()
order = manager.add_order(hawaiian_pizza)   # capture returned Order
manager.list_orders()
