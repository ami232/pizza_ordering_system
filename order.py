from pizza import PizzaFactory
from order import OrderManager


factory = PizzaFactory()
manager = OrderManager()

pizza1 = factory.create_margherita()
pizza2 = factory.create_pepperoni()
pizza3 = factory.create_custom("Veggie", ["tomato sauce", "mozzarella", "bell peppers", "onions", "olives"])
pizza4 = factory.create_hawaiian()

manager.add_order([pizza4])
manager.list_orders()

class SofiaPizzaFactory(PizzaFactoryAbstract):
    def create_margherita(self):
        return Pizza("Sofia Margherita", ["tomato sauce", "mozzarella", "basil", "oregano"])
    # Add more methods as needed

sofia_factory = SofiaPizzaFactory()
special_pizza = sofia_factory.create_special()
manager.add_order([special_pizza])
manager.list_orders()

class Order:
    def __init__(self, order_id, pizzas):
        self.order_id = order_id
        self.pizzas = pizzas
        self.status = "Pending"

    def __str__(self):
        pizza_names = ', '.join([pizza.name for pizza in self.pizzas])
        return f"Order #{self.order_id}: {pizza_names} | Status: {self.status}"

    def set_status(self, status):
        self.status = status

class OrderManager:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(OrderManager, cls).__new__(cls)
            cls.instance.orders = []
            cls.instance.next_order_id = 1
        return cls.instance

    def add_order(self, pizzas):
        order = Order(self.next_order_id, pizzas)
        self.orders.append(order)
        self.next_order_id += 1
        return order

    def list_orders(self):
        print("Current Orders:")
        for order in self.orders:
            print(order)
        print()

    def prepare_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                order.set_status("Preparing")
                for pizza in order.pizzas:
                    pizza.prepare()
                order.set_status("Completed")
                print(f"Order #{order_id} prepared and completed.")
                return
        print(f"Order #{order_id} not found.")

manager.prepare_order(1)
manager.list_orders()
