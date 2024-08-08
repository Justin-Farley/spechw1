class KitchenOrderStack:
    def __init__(self):
        self.stack = []
    
    def add_order(self, order):
        self.stack.append(order)
        print(f"Order added to kitchen: {order}")
    
    def complete_order(self):
        if not self.stack:
            print("No orders to complete.")
            return None
        completed_order = self.stack.pop()
        print(f"Order completed: {completed_order}")
        return completed_order
