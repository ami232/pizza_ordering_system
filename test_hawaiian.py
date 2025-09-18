# ...existing code...
from pizza import PizzaFactory
from order import OrderManager

factory = PizzaFactory()
manager = OrderManager()

hawaiian_pizza = factory.create_hawaiian()
hawaiian_pizza.prepare()  

manager.add_order(hawaiian_pizza)
manager.list_orders()


manager.prepare_order(1)
manager.list_orders()

#this hawaiian pizza works!