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

class Pizza:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
        self.prepared = False

    def prepare(self):
        self.prepared = True
        print(f"Pizza {self.name} is being prepared with ingredients: {', '.join(self.ingredients)}")

class PizzaFactoryAbstract:
    def create_margherita(self):
        raise NotImplementedError

    def create_pepperoni(self):
        raise NotImplementedError

    def create_special(self):
        raise NotImplementedError

class SofiaPizzaFactory(PizzaFactoryAbstract):
    def create_margherita(self):
        return Pizza("Sofia Margherita", ["tomato sauce", "mozzarella", "basil", "oregano"])
    def create_pepperoni(self):
        return Pizza("Sofia Pepperoni", ["tomato sauce", "mozzarella", "pepperoni", "jalapenos"])
    def create_special(self):
        return Pizza("Sofia Special", ["pesto sauce", "goat cheese", "sun-dried tomatoes"])