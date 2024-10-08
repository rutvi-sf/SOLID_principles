from abc import ABC, abstractmethod


# Class: Order (Responsible only for creating and storing order data)
class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items
        self.total_price = self.calculate_total()

    def create_order(self):
        print(f"Order created for {self.customer}. Total: {order.total_price}")

    def calculate_total(self):
        return sum(item['price'] for item in self.items)


# Class: InventoryManager (Handles inventory management)
class InventoryManager:
    def deduct_inventory(self, items):
        print("Deducting inventory for the items...")


# Class: PaymentProcessor (Handles payment processing)
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, customer, total_price):
        pass


class CashPaymentProcessor(PaymentProcessor):
    def __init__(self, customer, total_price):
        self.customer = customer
        self.total_price = total_price

    def process_payment(self, customer, total_price):
        print(f"Processing cash payment of {total_price} for {customer}...")
        return "SUCCESS"  # Assume payment is always successful


class ThirdPartyProcessor(ABC):
    @abstractmethod
    def process_payment(self, total_price):
        pass


class ThirdPartyPaymentProcessor(ThirdPartyProcessor):
    def __init__(self, total_price):
        self.total_price = total_price

    def process_payment(self, total_price):
        print(f"Processing third party payment of {total_price}")
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
cash_payment_processor = CashPaymentProcessor(customer, order.total_price)
cash_payment_processor.process_payment(customer, order.total_price)
third_party_payment_processor = ThirdPartyPaymentProcessor(order.total_price)
third_party_payment_processor.process_payment(order.total_price)
shipping = ShippingManager()
shipping.schedule_shipping(customer)
notification = NotificationService()
notification.send_notification(customer, "Order created successfully")
