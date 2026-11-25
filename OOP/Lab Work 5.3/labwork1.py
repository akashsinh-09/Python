class Car:
    def __init__(self,name,company,price):
        self.name=name
        self.company=company
        self.price=price
        
    def display(self):
        print("=====Details========")
        print("Name:",self.name)
        print("Company:",self.company)
        print("Price:",self.price)
    
car1=Car("Nexon","Tata","14 lakhs")

car1.display()
        
class Bike(Car):
    def __init__(self, name, company, price):
        self.name=name
        self.company=company
        self.price=price

bike1=Bike("Bullet 350","Royal Enfiled","2 lakhs")

bike1.display()