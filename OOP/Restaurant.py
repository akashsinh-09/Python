class Restautant:

    def __init__(self, restaurant_name, location, rating, food_type, contact_number):
        self.restaurant_name = restaurant_name
        self.location = location
        self.rating = rating
        self.food_type = food_type
        self.contact_number = contact_number

    def display(self):

        print("Restaurant Name:", self.restaurant_name)
        print("Location:", self.location)
        print("Rating:", self.rating)
        print("Food Type:", self.food_type)
        print("Contact Number:", self.contact_number)



restaurant1 = Restautant("Honest", "Rajkot", 4.2, "Fast Food", "9876543210")
restaurant2 = Restautant("McDonald's", "Ahmedabad", 4.5, "Burgers", "9876543211")
restaurant3 = Restautant("Domino's Pizza", "Mumbai", 4.3, "Pizza", "9876543212")
restaurant4 = Restautant("The Grand Thakar", "Rajkot", 4.4, "Gujarati", "9876543213")
restaurant5 = Restautant("Subway", "Surat", 4.1, "Sandwiches", "9876543214")



restaurant1.display()
print("----------------------")

restaurant2.display()
print("----------------------")

restaurant3.display()
print("----------------------")

restaurant4.display()
print("----------------------")

restaurant5.display()