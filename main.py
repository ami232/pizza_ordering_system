from pizza import PizzaFactory, ItalianPizzaFactory, AmericanPizzaFactory, GeorgePizzaFactory
from order import OrderManager

print("=== Pizza Ordering System Demo ===\n")

factory = PizzaFactory()
manager = OrderManager()

# Step 1: Place Orders - Create different pizza types
print("Step 1: Creating and ordering different pizzas...")
margherita = factory.create_margherita()
pepperoni = factory.create_pepperoni()
veggie = factory.create_veggie()  # Added in Step 1
hawaiian = factory.create_hawaiian()  # Added in Step 2

manager.add_order([margherita])
manager.add_order([pepperoni])
manager.add_order([veggie])
manager.add_order([hawaiian])

print("Orders placed!")
manager.list_orders()

# Step 3: Prepare Orders
print("Step 3: Preparing orders...")
manager.prepare_order(1)  # Prepare Margherita
manager.prepare_order(2)  # Prepare Pepperoni

print("\nOrders after preparation:")
manager.list_orders()

# Abstract Factory Demo
print("=== Abstract Factory Demo ===")
italian_factory = ItalianPizzaFactory()
american_factory = AmericanPizzaFactory()

italian_pizza = italian_factory.create_margherita()
american_pizza = american_factory.create_margherita()

manager.add_order([italian_pizza])
manager.add_order([american_pizza])

# Step 4: George's Custom Pizza Factory
print("\n=== Step 4: George's Custom Pizza Factory ===")
george_factory = GeorgePizzaFactory()

george_margherita = george_factory.create_margherita()
george_pepperoni = george_factory.create_pepperoni()
george_bbq_chicken = george_factory.create_bbq_chicken()  # Signature pizza

manager.add_order([george_margherita])
manager.add_order([george_pepperoni])
manager.add_order([george_bbq_chicken])

print("All orders including George's custom pizzas:")
manager.list_orders()

print("Preparing George's signature BBQ Chicken pizza:")
manager.prepare_order(8)  # BBQ Chicken order