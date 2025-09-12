from pizza import PizzaFactory
from order import OrderManager

factory = PizzaFactory()

margherita = factory.create_margherita()
pepperoni = factory.create_pepperoni()
veggie = factory.create_custom(
    "Veggie",
    ["tomato sauce", "mozzarella", "bell peppers", "olives", "onions"]
)

manager = OrderManager()
order = manager.add_order([margherita, pepperoni, veggie])

print(margherita)
print(pepperoni)
print(veggie)

print(f"Created Order #{order.order_id}")
manager.list_orders()