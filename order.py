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
        for order in self.orders:
            if order.order_id == order_id:
                print(f"\nPreparing order #{order_id}:")
                for pizza in order.pizzas:
                    pizza.prepare()
                return
        print(f"Order {order_id} not found!")

    def dispatch_order(self, order_id):
        pass
