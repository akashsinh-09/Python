class Pharmcy:

    def __init__(self, medicine_name, company_name, medicine_type, price, expiry_date):
        self.medicine_name = medicine_name
        self.company_name = company_name
        self.medicine_type = medicine_type
        self.price = price
        self.expiry_date = expiry_date

    def display(self):

        print("Medicine Name:", self.medicine_name)
        print("Company Name:", self.company_name)
        print("Medicine Type:", self.medicine_type)
        print("Price:", self.price)
        print("Expiry Date:", self.expiry_date)


medicine1 = Pharmcy("Paracetamol", "Cipla", "Tablet", 30, "12-2027")
medicine2 = Pharmcy("Cetirizine", "Dr. Reddy's", "Tablet", 45, "06-2027")
medicine3 = Pharmcy("Crocin", "GSK", "Tablet", 25, "09-2027")
medicine4 = Pharmcy("Benadryl", "Johnson & Johnson", "Syrup", 120, "03-2028")
medicine5 = Pharmcy("Volini", "Sun Pharma", "Gel", 110, "11-2027")


medicine1.display()
print("----------------------")

medicine2.display()
print("----------------------")

medicine3.display()
print("----------------------")

medicine4.display()
print("----------------------")

medicine5.display()