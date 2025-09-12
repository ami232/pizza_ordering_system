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
        # Normalize input to a list to support passing a single Pizza
        
        if pizzas is None:
            pizzas_list = []
        elif isinstance(pizzas, list):
            pizzas_list = pizzas
        else:
            pizzas_list = [pizzas]

        order_id = self.next_order_id
        order = Order(order_id, pizzas_list)
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
                print(f"Preparing Order #{order_id}:")
                for pizza in order.pizzas:
                    pizza.prepare()
                print(f"Order #{order_id} prepared.\n")
                return order
        print(f"Order #{order_id} not found.\n")
        return None

    def dispatch_order(self, order_id):
        for idx, order in enumerate(self.orders):
            if order.order_id == order_id:
                if not all(pizza.prepared for pizza in order.pizzas):
                    print(
                        f"Order #{order_id} cannot be dispatched: not all pizzas are prepared.\n"
                    )
                    return None
                print(f"Dispatching Order #{order_id}...")
                self.orders.pop(idx)
                print(f"Order #{order_id} dispatched.\n")
                return order
        print(f"Order #{order_id} not found.\n")
        return None
