sofia_extra_delivery
from pizza import Pizza


from typing import Iterable
from pizza import Pizza


main
class Order:
    def __init__(self, order_id, pizzas):
        self.order_id = order_id
        self.pizzas = pizzas
        self.status = "Pending"
        self.delivery_status = "Not Dispatched"

    def __str__(self):
        pizza_names = ', '.join([pizza.name for pizza in self.pizzas])
        return f"Order #{self.order_id}: {pizza_names} | Status: {self.status} | Delivery: {self.delivery_status}"

    def set_status(self, status):
        self.status = status

    def set_delivery_status(self, delivery_status):
        self.delivery_status = delivery_status

class OrderManager:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(OrderManager, cls).__new__(cls)
            cls.instance.orders = []
            cls.instance.next_order_id = 1
        return cls.instance

    def add_order(self, pizzas: Iterable[Pizza]):
        order_id = self.next_order_id
        order = Order(order_id, pizzas)
        self.orders.append(order)
        self.next_order_id += 1
        return orde

sofia_extra_delivery
    def add_order(self, pizzas):

    def add_order(self, pizzas: Iterable[Pizza]):
main
        order_id = self.next_order_id
        order = Order(order_id, pizzas)
        self.orders.append(order)
        self.next_order_id += 1
        return order

    def list_orders(self):
        print("Current Orders:")
        for order in self.orders:
            print(order)
        print()

    def dispatch_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                order.set_delivery_status("Out for Delivery")
                print(f"Order #{order_id} is out for delivery.")
                return
        print(f"Order #{order_id} not found.")

    def deliver_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                order.set_delivery_status("Delivered")
                print(f"Order #{order_id} has been delivered.")
                return
        print(f"Order #{order_id} not found.")

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