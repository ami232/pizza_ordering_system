from pizza import PizzaFactory, ItalianPizzaFactory, AmericanPizzaFactory
from order import OrderManager

def main():
    factory = PizzaFactory()
    manager = OrderManager()

    # Step 1 - Create and order different pizzas
    print("Creating different pizzas:")
    margherita = factory.create_margherita()
    pepperoni = factory.create_pepperoni()
    veggie = factory.create_veggie()
    hawaiian = factory.create_hawaiian()

    # Add to order manager
    manager.add_order([margherita, pepperoni])
    manager.add_order([veggie, hawaiian])
    
    print("\nInitial orders:")
    manager.list_orders()

    # Prepare orders
    print("\nPreparing orders:")
    manager.prepare_order(1)
    manager.prepare_order(2)
    
    print("\nFinal order status:")
    manager.list_orders()

if __name__ == "__main__":
    main()