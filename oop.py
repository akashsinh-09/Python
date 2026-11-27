class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        
        
mb1=Mobile("Samsung",65000)
mb2=Mobile("Apple",75000)

print(f"The {mb1.brand}'s moblie price is {mb1.price}")
print(f"The {mb2.brand}'s moblie price is {mb2.price}")        