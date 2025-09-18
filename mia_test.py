from pizza import MiaPizzaFactory
from order import OrderManager

factory = MiaPizzaFactory()
manager = OrderManager()

bbq_pizza = factory.create_bbq()
manager.add_order([bbq_pizza])
manager.list_orders()

manager.prepare_order(1)
manager.list_orders()
