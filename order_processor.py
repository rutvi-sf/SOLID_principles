class OrderManager:
    def create_order(self, customer, items):
        # Step 1: Create an order
        print(f"Creating order for {customer}")
        total = self.calculate_total(items)
        print(f"Total price: {total}")

        # Step 2: Deduct inventory
        self.deduct_inventory(items)

        # Step 3: Process payment
        payment_status = self.process_payment(customer, total)
        if payment_status == "SUCCESS":
            # Step 4: Schedule shipping
            self.schedule_shipping(customer)

            # Step 5: Send notification
            self.send_notification(customer, "Order created successfully")
            print("Order completed successfully.")
        else:
            print("Order failed due to payment issues.")

    def calculate_total(self, items):
        return sum(item['price'] for item in items)

    def deduct_inventory(self, items):
        print("Deducting inventory for the items...")

    def process_payment(self, customer, total):
        print(f"Processing payment of {total} for {customer}...")
        return "SUCCESS"  # Assume payment is always successful

    def schedule_shipping(self, customer):
        print(f"Scheduling shipping for {customer}...")

    def send_notification(self, customer, message):
        print(f"Sending notification to {customer}: {message}")


order_manager = OrderManager()
customer = "John Doe"
items = [{"name": "Laptop", "price": 1000}, {"name": "Mouse", "price": 50}]
order_manager.create_order(customer, items)
