class Online_order:
    
    def __init__(self,order_id,customer_name,order_date,total_amount,payment_status):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date= order_date
        self.total_amount = total_amount
        self.payment_status = payment_status
        
    def display(self):
        
        print("Order ID:",self.order_id)
        print("Customer Name:",self.customer_name)
        print("Order Date:",self.order_date)
        print("Total Amount:",self.total_amount)
        print("Payment Status:",self.payment_status)

order1 = Online_order(101, "Rahul", "24-11-2026", 1500, "Paid")
order2 = Online_order(102, "Amit", "24-11-2026", 2500, "Pending")
order3 = Online_order(103, "Priya", "23-11-2026", 3200, "Paid")
order4 = Online_order(104, "Neha", "22-11-2026", 1800, "Failed")
order5 = Online_order(105, "Karan", "21-11-2026", 4500, "Paid")

order1.display()
print()
order2.display()
print()
order3.display()
print()
order4.display()
print()
order5.display()
print()
