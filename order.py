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

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OrderManager, cls).__new__(cls)
            cls._instance.orders = []
            cls._instance.next_order_id = 1
        return cls._instance

    def add_order(self, pizzas):
        # Handle both single pizza and list of pizzas
        if not isinstance(pizzas, list):
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
        for order in self.orders:
            if order.order_id == order_id:
                print(f"Preparing Order #{order_id}:")
                for pizza in order.pizzas:
                    pizza.prepare()
                print(f"Order #{order_id} is ready!\n")
                return
        print(f"Order #{order_id} not found!")

    def dispatch_order(self, order_id):
        for i, order in enumerate(self.orders):
            if order.order_id == order_id:
                # Check if all pizzas are prepared
                all_prepared = all(pizza.prepared for pizza in order.pizzas)
                if all_prepared:
                    print(f"Dispatching Order #{order_id} for delivery!")
                    # Remove the order from the list as it's been dispatched
                    self.orders.pop(i)
                    return
                else:
                    print(f"Order #{order_id} cannot be dispatched - not all pizzas are prepared!")
                    return
        print(f"Order #{order_id} not found!")
