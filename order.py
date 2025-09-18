from typing import Iterable
from pizza import Pizza


class Order:
    def __init__(self, order_id: int, pizzas: Iterable[Pizza]):
        self.order_id = order_id
        self.pizzas = list(pizzas)

    def __str__(self):
        order_str = "Order #" + str(self.order_id) + ":\n"
        for pizza in self.pizzas:
            order_str += "- " + str(pizza) + "\n"
        return order_str


class OrderManager:
    _instance = None
    orders: list[Order]
    next_order_id: int

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OrderManager, cls).__new__(cls)
            cls._instance.orders = []
            cls._instance.next_order_id = 1
        return cls._instance

    def _get_order(self, order_id: int) -> Order | None:
        for o in self.orders:
            if o.order_id == order_id:
                return o
        return None

    def add_order(self, pizzas: Iterable[Pizza]) -> Order:
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


    def prepare_order(self, order_id: int):
        order = self._get_order(order_id)
        if not order:
            print(f"Order #{order_id} not found.")
            return
        print(f"Preparing Order #{order_id}...")
        for pizza in order.pizzas:
            pizza.prepare()
        print(f"Order #{order_id} prepared.\n")


    def dispatch_order(self, order_id: int):
        order = self._get_order(order_id)
        if not order:
            print(f"Order #{order_id} not found.")
            return
        print(f"Dispatching Order #{order_id}... Done!\n")

