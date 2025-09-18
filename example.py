from pizza import PizzaFactory, ItalianPizzaFactory, AmericanPizzaFactory
from order import OrderManager

def main():
    print("=== Pizza Ordering System Demo ===\n")
    
    # Get OrderManager instance (Singleton)
    manager = OrderManager()
    
    # Step 1: Create pizzas using PizzaFactory
    print("Step 1: Creating pizzas with PizzaFactory")
    factory = PizzaFactory()
    
    margherita = factory.create_margherita()
    pepperoni = factory.create_pepperoni()
    veggie = factory.create_veggie()
    
    # Add pizzas to order manager
    order1 = manager.add_order(margherita)
    order2 = manager.add_order(pepperoni)
    order3 = manager.add_order(veggie)
    
    # List current orders
    manager.list_orders()
    
    # Step 2: Add Hawaiian pizza
    print("Step 2: Adding Hawaiian pizza")
    hawaiian = factory.create_hawaiian()
    order4 = manager.add_order(hawaiian)
    manager.list_orders()
    
    # Step 3: Prepare some orders
    print("Step 3: Preparing orders")
    manager.prepare_order(order1)
    manager.prepare_order(order3)
    manager.list_orders()

if __name__ == "__main__":
    main()
