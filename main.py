from pizza import PizzaFactory
from order import OrderManager

factory = PizzaFactory()

margherita = factory.create_margherita()
pepperoni = factory.create_pepperoni()
veggie = factory.create_custom(
    "Veggie",
    ["tomato sauce", "mozzarella", "bell peppers", "olives", "onions"]
)

hawaiian = factory.create_hawaiian()

manager = OrderManager()
order = manager.add_order([margherita, pepperoni, veggie])

print(margherita)
print(pepperoni)
print(veggie)
print(hawaiian)

print(f"Created Order #{order.order_id}")

from pizza import PizzaFactory, ItalianPizzaFactory, AmericanPizzaFactory
from order import OrderManager

factory = PizzaFactory()
manager = OrderManager()

# Factory Method
pizza = factory.create_margherita()
manager.add_order([pizza])
manager.list_orders()
manager.prepare_order(1)

# Abstract Factory
italian_factory = ItalianPizzaFactory()
american_factory = AmericanPizzaFactory()

italian_pizza = italian_factory.create_margherita()
american_pizza = american_factory.create_margherita()

manager.add_order([italian_pizza])
manager.add_order([american_pizza])
manager.list_orders()


hawaiian_only_order = manager.add_order([hawaiian])
print(f"Created Order #{hawaiian_only_order.order_id} (Hawaiian only)")

print("\nBefore preparing Hawaiian:")
manager.list_orders()

manager.prepare_order(hawaiian_only_order.order_id)

print("After preparing Hawaiian:")
manager.list_orders()

for p in hawaiian_only_order.pizzas:
    print(f"{p.name} prepared? {p.prepared}")