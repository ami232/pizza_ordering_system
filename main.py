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
from factory import AdriPizzaFactory

if __name__ == "__main__":
    f = AdriPizzaFactory()
    bbq = f.create_pizza("bbq_chicken")
    print("Created:", bbq.name, bbq.ingredients)
    bbq.prepare()
    print("Prepared?", bbq.prepared)
