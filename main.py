from pizza import PizzaFactory

factory = PizzaFactory()

margherita = factory.create_margherita()
pepperoni = factory.create_pepperoni()
veggie = factory.create_custom("Veggie", ["tomato sauce ", "mozzarella", "bell peppers", "olives", "onions"])

print(margherita)
print(pepperoni)
print(veggie)