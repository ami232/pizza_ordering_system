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

    def add_order(self, pizzas):
        # accept either a single Pizza or a list/tuple of pizzas
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
        # find the order by id
        for order in self.orders:
            if order.order_id == order_id:
                print(f"Preparing Order #{order_id}")
                for pizza in order.pizzas:
                    pizza.prepare()  # calls Pizza.prepare()
                return True
        print(f"Order #{order_id} not found")
        return False

    def dispatch_order(self, order_id):
        # optional bonus: remove an order once all pizzas are prepared
        for i, order in enumerate(self.orders):
            if order.order_id == order_id:
                if all(p.prepared for p in order.pizzas):
                    print(f"Dispatching Order #{order_id}")
                    self.orders.pop(i)
                    return True
                else:
                    print(f"Order #{order_id} is not fully prepared")
                    return False
        print(f"Order #{order_id} not found")
        return False
