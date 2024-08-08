# customer_order_queue.py

from collections import deque

class CustomerOrderQueue:
    def __init__(self):
        self.queue = deque()
    
    def add_order(self, order, priority=0):
        self.queue.append((priority, order))
        self.queue = deque(sorted(self.queue, key=lambda x: -x[0]))
        print(f"Order added to customer queue: {order}")
    
    def process_order(self):
        if not self.queue:
            print("No orders to process.")
            return None
        _, processed_order = self.queue.popleft()
        print(f"Order processed: {processed_order}")
        return processed_order
