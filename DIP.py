from abc import ABC, abstractmethod


# Interfaces
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, customer, total_price):
        pass

class InventoryManager(ABC):
    
    @abstractmethod
    def deduct_inventory(self, items):
        pass

class ShippingManager(ABC):
    @abstractmethod
    def schedule_shipping(self, customer):
        pass


class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, customer, message):
        pass


# Implementations of the interfaces
class CashPaymentProcessor(PaymentProcessor):
    def __init__(self):
        pass

    def process_payment(self, customer, total_price):
        print(f"Processing cash payment of {total_price} for {customer}...")
        return "SUCCESS"  # Assume payment is always successful


class ThirdPartyPaymentProcessor(PaymentProcessor):
    def __init__(self):
        pass

    def process_payment(self, customer, total_price):
        print(f"Processing third party payment of {total_price} for {customer}...")
        return "SUCCESS"  # Assume payment is always successful


class SimpleInventoryManager(InventoryManager):
    def deduct_inventory(self, items):
        print("Deducting inventory for the items...")

class SimpleShippingManager(ShippingManager):
    def schedule_shipping(self, customer):
        print(f"Scheduling shipping for {customer}...")


class SimpleNotificationService(NotificationService):
    def send_notification(self, customer, message):
        print(f"Sending notification to {customer}: {message}")


# Class: Order (Responsible only for creating and storing order data)
class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items
        self.total_price = self.calculate_total()

    def create_order(self):
        # Step 1: Create the order
        print(f"Order created for {self.customer}. Total: {self.total_price}")

    def calculate_total(self):
        return sum(item['price'] for item in self.items)


class OrderProcessor:
    def __init__(self, payment_processor: PaymentProcessor,
                 inventory_manager: InventoryManager,
                 shipping_manager: ShippingManager,
                 notification_service: NotificationService):
        self.payment_processor = payment_processor
        self.inventory_manager = inventory_manager
        self.shipping_manager = shipping_manager
        self.notification_service = notification_service

    def process_order(self, order: Order):
        # Creating the order
        order.create_order()

        inventory_manager.deduct_inventory(order.items)
        # Processing payment
        self.payment_processor.process_payment(order.customer, order.total_price)

        # Scheduling shipping
        self.shipping_manager.schedule_shipping(order.customer)

        # Sending notification
        self.notification_service.send_notification(order.customer, "Order created successfully")


customer = "John Doe"
items = [{"name": "Laptop", "price": 1000}, {"name": "Mouse", "price": 50}]
order = Order(customer, items)

cash_payment_processor = CashPaymentProcessor()
shipping_manager = SimpleShippingManager()
inventory_manager = SimpleInventoryManager()
notification_service = SimpleNotificationService()

order_processor = OrderProcessor(cash_payment_processor, inventory_manager, shipping_manager, notification_service)
order_processor.process_order(order)
