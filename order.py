from typing import Iterable
from pizza import Pizza

class Order:
    def __init__(self, order_id, pizzas):
        self.order_id = order_id
        self.pizzas = pizzas
<<<<<<< HEAD
        self.status = "NEW"

    def __str__(self):
        order_str = f"Order #{self.order_id} [{self.status}]:\n"
        for pizza in self.pizzas:
            order_str += "- " + str(pizza) + "\n"
        return order_str
=======
        self.status = "Pending"
        self.delivery_status = "Not Dispatched"

    def __str__(self):
        pizza_names = ', '.join([pizza.name for pizza in self.pizzas])
        return f"Order #{self.order_id}: {pizza_names} | Status: {self.status} | Delivery: {self.delivery_status}"

    def set_status(self, status):
        self.status = status

    def set_delivery_status(self, delivery_status):
        self.delivery_status = delivery_status
>>>>>>> main


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
        # accept a single Pizza or an iterable of pizzas, only for testing the hawaiian pizza creating
        
        if not isinstance(pizzas, (list, tuple)):
            pizzas = [pizzas]
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
<<<<<<< HEAD
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
        order.status = "PREPARED"
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
        order.status = "DISPATCHED"
        print(f"Order #{order_id} dispatched! 🍕🚚\n")
        return True
=======
        for order in self.orders:
            if order.order_id == order_id:
                order.set_status("Preparing")
                for pizza in order.pizzas:
                    pizza.prepare()
                order.set_status("Completed")
                print(f"Order #{order_id} prepared and completed.")
                return
        print(f"Order #{order_id} not found.")

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
>>>>>>> main
