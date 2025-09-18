from typing import Iterable
from pizza import Pizza


class Order:
    def __init__(self, order_id, pizzas):
        self.order_id = order_id
        self.pizzas = pizzas

    def __str__(self):
        order_str = "Order #" + str(self.order_id) + ":\n"
        for pizza in self.pizzas:
            order_str += "- " + str(pizza) + "\n"
        return order_str


class OrderManager:
    _instance = None
    orders = []
    next_order_id: int

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OrderManager, cls).__new__(cls)
            cls._instance.orders = []
            cls._instance.next_order_id = 1
        return cls._instance

    def add_order(self, pizzas: Iterable[Pizza]):
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

    def prepare_order(self, order_id):
        """
        Prepare all pizzas in the given order.
        Returns True if order found and prepared (even if already prepared), False if not found.
        """
        order = self._find_order(order_id)
        if order is None:
            print(f"Order #{order_id} not found.")
            return False

        print(f"Preparing Order #{order_id} ...")
        for p in order.pizzas:
            p.prepare()
        print(f"Order #{order_id} is prepared.\n")
        return True

    def dispatch_order(self, order_id):
        """
        (Bonus) Dispatch order only if all pizzas are prepared; remove it from the queue.
        """
        order = self._find_order(order_id)
        if order is None:
            print(f"Order #{order_id} not found.")
            return False

        all_prepared = all(p.prepared for p in order.pizzas)
        if not all_prepared:
            print(f"Order #{order_id} cannot be dispatched: not all pizzas are prepared.")
            return False

        self.orders = [o for o in self.orders if o.order_id != order_id]
        print(f"Order #{order_id} dispatched! 🍕🚚\n")
        return True
