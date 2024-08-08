from kitchen_order_stack import KitchenOrderStack
from customer_order_queue import CustomerOrderQueue

def test_order_management_system():
    kitchen_stack = KitchenOrderStack()
    customer_queue = CustomerOrderQueue()
    
    
    customer_queue.add_order("Order 1", priority=1)
    customer_queue.add_order("Order 2", priority=2)
    
    
    order_to_kitchen = customer_queue.process_order()
    kitchen_stack.add_order(order_to_kitchen)
    
    # Complete orders in the kitchen
    kitchen_stack.complete_order()
    
    
    customer_queue.add_order("Order 3", priority=1)
    customer_queue.add_order("Order 4", priority=3)
    
    order_to_kitchen = customer_queue.process_order()
    kitchen_stack.add_order(order_to_kitchen)
    
    kitchen_stack.complete_order()

if __name__ == "__main__":
    test_order_management_system()
