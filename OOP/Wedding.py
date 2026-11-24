class Wedding:

    def __init__(self, bride_name, groom_name, wedding_date, wedding_location, total_guests):
        self.bride_name = bride_name
        self.groom_name = groom_name
        self.wedding_date = wedding_date
        self.wedding_location = wedding_location
        self.total_guests = total_guests

    def display(self):

        print("Bride Name:", self.bride_name)
        print("Groom Name:", self.groom_name)
        print("Wedding Date:", self.wedding_date)
        print("Wedding Location:", self.wedding_location)
        print("Total Guests:", self.total_guests)



wedding1 = Wedding("Priya", "Rahul", "15-12-2026", "Rajkot", 500)
wedding2 = Wedding("Neha", "Amit", "20-12-2026", "Ahmedabad", 800)
wedding3 = Wedding("Riya", "Karan", "05-01-2027", "Surat", 300)
wedding4 = Wedding("Pooja", "Jay", "12-02-2027", "Mumbai", 1000)
wedding5 = Wedding("Anjali", "Rohit", "25-02-2027", "Jaipur", 600)


wedding1.display()
print("----------------------")

wedding2.display()
print("----------------------")

wedding3.display()
print("----------------------")

wedding4.display()
print("----------------------")

wedding5.display()