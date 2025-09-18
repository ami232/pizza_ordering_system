class OrderManager:
    """
    Singleton pattern: Only one instance of OrderManager can exist.
    Manages all pizza orders in the system.
    """
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OrderManager, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not OrderManager._initialized:
            self.orders = {}
            self.order_counter = 0
            OrderManager._initialized = True
    
    def add_order(self, pizza):
        """Add a new pizza order to the system"""
        self.order_counter += 1
        order_id = self.order_counter
        self.orders[order_id] = pizza
        print(f"Order #{order_id} added: {pizza.name}")
        return order_id
    
    def list_orders(self):
        """Display all current orders"""
        if not self.orders:
            print("No orders found.")
            return
        
        print("\n=== Current Orders ===")
        for order_id, pizza in self.orders.items():
            print(f"Order #{order_id}: {pizza}")
        print("=====================\n")
    
    def prepare_order(self, order_id):
        """Prepare a specific order by order ID"""
        if order_id in self.orders:
            pizza = self.orders[order_id]
            pizza.prepare()
            print(f"Order #{order_id} preparation completed!")
        else:
            print(f"Order #{order_id} not found.")
    
    def get_order(self, order_id):
        """Get a specific order by ID"""
        return self.orders.get(order_id, None)
    
    def get_total_orders(self):
        """Get total number of orders"""
        return len(self.orders)
