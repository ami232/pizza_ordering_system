from pizza import PizzaFactory, ItalianPizzaFactory, AmericanPizzaFactory
from order import OrderManager

# Create factories and manager
factory = PizzaFactory()
manager = OrderManager()

# ---------- Simple Factory Orders ----------
margherita = factory.create_margherita()
pepperoni = factory.create_pepperoni()
veggie = factory.create_veggie()
hawaiian = factory.create_hawaiian()

manager.add_order([margherita])
manager.add_order([pepperoni])
manager.add_order([veggie])
manager.add_order([hawaiian])

manager.list_orders()
manager.prepare_order(1)

# ---------- Abstract Factory Orders ----------
italian_factory = ItalianPizzaFactory()
american_factory = AmericanPizzaFactory()

italian_hawaiian = italian_factory.create_hawaiian()
american_veggie = american_factory.create_veggie()
italian_pizza = italian_factory.create_margherita()
american_pizza = american_factory.create_margherita()

manager.add_order([italian_hawaiian])
manager.add_order([american_veggie])
manager.add_order([italian_pizza])
manager.add_order([american_pizza])

manager.list_orders()
manager.prepare_order(5)
manager.dispatch_order(5)
