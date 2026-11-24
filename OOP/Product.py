class Product:

    def __init__(self, product_id, product_name, category, price, quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.price = price
        self.quantity = quantity

    def display(self):

        print("Product ID:", self.product_id)
        print("Product Name:", self.product_name)
        print("Category:", self.category)
        print("Price:", self.price)
        print("Quantity:", self.quantity)


product1 = Product(101, "Laptop", "Electronics", 55000, 10)
product2 = Product(102, "T-Shirt", "Clothing", 799, 50)
product3 = Product(103, "Office Chair", "Furniture", 4500, 15)
product4 = Product(104, "Notebook", "Stationery", 80, 100)
product5 = Product(105, "Headphones", "Electronics", 1999, 25)


product1.display()
print("----------------------")

product2.display()
print("----------------------")

product3.display()
print("----------------------")

product4.display()
print("----------------------")

product5.display()