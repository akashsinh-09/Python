class Fashion_product:

    def __init__(self, product_name, brand, size, color, price):
        self.product_name = product_name
        self.brand = brand
        self.size = size
        self.color = color
        self.price = price

    def display(self):

        print("Product Name:", self.product_name)
        print("Brand:", self.brand)
        print("Size:", self.size)
        print("Color:", self.color)
        print("Price:", self.price)


product1 = Fashion_product("T-Shirt", "Nike", "M", "Black", 999)
product2 = Fashion_product("Jeans", "Levis", "32", "Blue", 1999)
product3 = Fashion_product("Jacket", "Puma", "L", "Grey", 2499)
product4 = Fashion_product("Sneakers", "Adidas", "9", "White", 3499)
product5 = Fashion_product("Shirt", "Zara", "XL", "Green", 1599)


product1.display()
print("----------------------")

product2.display()
print("----------------------")

product3.display()
print("----------------------")

product4.display()
print("----------------------")

product5.display()