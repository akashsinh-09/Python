class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def vehicle_info(self):
        print("Vehilce Brand:",self.brand)
        print("Model :",self.model)

class Car(Vehicle):
    def __init__(self, brand, model,fuel_type,):
        super().__init__(brand, model)
        self.fuel_type=fuel_type

    def car_info(self):
        self.vehicle_info()
        print("Fuel Type:",self.fuel_type)

class ElectricCar(Car):
    def __init__(self, brand, model, fuel_type,battery_capacity):
        super().__init__(brand, model, fuel_type)
        self.battery_capacity=battery_capacity
        
    def electric_car_info(self):
        self.car_info()
        print("Battery Capacity:",self.battery_capacity)
        
car1 = ElectricCar("Tesla", "Model 3", "Electric", "75 kWh")

car1.electric_car_info()
        
