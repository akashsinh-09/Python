class Electronic_device:

    def __init__(self, device_name, brand, model, price, warranty):
        self.device_name = device_name
        self.brand = brand
        self.model = model
        self.price = price
        self.warranty = warranty

    def display(self):

        print("Device Name:", self.device_name)
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
        print("Warranty:", self.warranty)


device1 = Electronic_device("Smartphone", "Samsung", "Galaxy A14 5G", 15000, "1 Year")
device2 = Electronic_device("Laptop", "Dell", "Inspiron 15", 55000, "2 Years")
device3 = Electronic_device("Smart TV", "Sony", "Bravia 4K", 45000, "2 Years")
device4 = Electronic_device("Headphones", "Boat", "Rockerz 450", 1500, "1 Year")
device5 = Electronic_device("Smartwatch", "Noise", "ColorFit Pro 5", 3500, "1 Year")


device1.display()
print("----------------------")

device2.display()
print("----------------------")

device3.display()
print("----------------------")

device4.display()
print("----------------------")

device5.display()