#!/usr/bin/env python3
"""
Test script to demonstrate the pizza ordering system functionality
"""

from pizza import PizzaFactory, ItalianPizzaFactory, AmericanPizzaFactory
from order import OrderManager

def main():
    print("=== Pizza Ordering System Test ===\n")
    
    # Create factory and manager instances
    factory = PizzaFactory()
    italian_factory = ItalianPizzaFactory()
    american_factory = AmericanPizzaFactory()
    manager = OrderManager()
    
    print("1. Creating pizzas using different factories...")
    # Create pizzas using different factories
    margherita = factory.create_margherita()
    pepperoni = factory.create_pepperoni()
    italian_margherita = italian_factory.create_margherita()
    american_pepperoni = american_factory.create_pepperoni()
    custom_pizza = factory.create_custom("Veggie Supreme", ["tomato sauce", "mozzarella", "bell peppers", "mushrooms", "olives"])
    
    print("✓ Pizzas created successfully\n")
    
    print("2. Adding orders to the system...")
    # Add orders (testing both single pizza and multiple pizzas)
    order1 = manager.add_order(margherita)  # Single pizza
    order2 = manager.add_order([pepperoni, italian_margherita])  # Multiple pizzas
    order3 = manager.add_order(american_pepperoni)  # Single pizza
    order4 = manager.add_order([custom_pizza])  # Single pizza in list
    
    print("✓ Orders added successfully\n")
    
    print("3. Listing all orders...")
    manager.list_orders()
    
    print("4. Preparing orders...")
    manager.prepare_order(1)
    manager.prepare_order(2)
    manager.prepare_order(3)
    
    print("5. Listing orders after preparation...")
    manager.list_orders()
    
    print("6. Testing dispatch functionality...")
    # Try to dispatch prepared orders
    manager.dispatch_order(1)
    manager.dispatch_order(2)
    
    # Try to dispatch unprepared order (should fail)
    manager.dispatch_order(4)
    
    print("7. Final order list (after dispatching)...")
    manager.list_orders()
    
    print("8. Testing singleton pattern...")
    # Test that OrderManager is truly a singleton
    manager2 = OrderManager()
    print(f"Same instance? {manager is manager2}")
    print(f"Orders count in manager2: {len(manager2.orders)}")
    
    print("\n=== Test Complete ===")

if __name__ == "__main__":
    main()
