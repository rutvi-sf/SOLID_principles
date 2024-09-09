# Class: Order (Responsible only for creating and storing order data)
class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items
        self.total_price = self.calculate_total()

    def create_order(self):
        # Step 1: Create the order
        print(f"Order created for {self.customer}. Total: {order.total_price}")

    def calculate_total(self):
        return sum(item['price'] for item in self.items)


# Class: InventoryManager (Handles inventory management)
class InventoryManager:
    def deduct_inventory(self, items):
        print("Deducting inventory for the items...")


# Class: PaymentProcessor (Handles payment processing)
class PaymentProcessor:
    def process_payment(self, customer, total_price):
        print(f"Processing payment of {total_price} for {customer}...")
        return "SUCCESS"  # Assume payment is always successful


# Class: ShippingManager (Handles shipping)
class ShippingManager:
    def schedule_shipping(self, customer):
        print(f"Scheduling shipping for {customer}...")


# Class: NotificationService (Handles customer notifications)
class NotificationService:
    def send_notification(self, customer, message):
        print(f"Sending notification to {customer}: {message}")


customer = "John Doe"
items = [{"name": "Laptop", "price": 1000}, {"name": "Mouse", "price": 50}]
order = Order(customer, items)
order.create_order()
inventory_manager = InventoryManager()
inventory_manager.deduct_inventory(order.items)
payment_processor = PaymentProcessor()
payment_processor.process_payment(customer, order.total_price)
shipping = ShippingManager()
shipping.schedule_shipping(customer)
notification = NotificationService()
notification.send_notification(customer, "Order created successfully")
