from pizza import SofiaPizzaFactory


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
                for pizza in order.pizzas:
                    pizza.prepare()
                print(f"Order #{order_id} prepared.")
                return
        print(f"Order #{order_id} not found.")

    def dispatch_order(self, order_id):
        pass

    def create_hawaiian(self):
        return Pizza("Hawaiian", ["tomato sauce", "mozzarella", "ham", "pineapple"])


class SofiaPizzaFactory(PizzaFactoryAbstract):
    def create_margherita(self):
        return Pizza("Sofia Margherita", ["tomato sauce", "mozzarella", "basil", "oregano"])

    def create_pepperoni(self):
        return Pizza("Sofia Pepperoni", ["tomato sauce", "mozzarella", "pepperoni", "chili flakes"])

    def create_special(self):
        return Pizza("Sofia Special", ["pesto sauce", "goat cheese", "sun-dried tomatoes"])


manager = OrderManager()
factory = OrderManager()

pizza4 = factory.create_hawaiian()
manager.add_order([pizza4])
manager.list_orders()

sofia_factory = SofiaPizzaFactory()
special_pizza = sofia_factory.create_special()
manager.add_order([special_pizza])
manager.list_orders()
