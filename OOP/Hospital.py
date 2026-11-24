class Hospital:

    def __init__(self, hospital_name, location, total_beds, contact_number, specialization):
        self.hospital_name = hospital_name
        self.location = location
        self.total_beds = total_beds
        self.contact_number = contact_number
        self.specialization = specialization

    def display(self):

        print("Hospital Name:", self.hospital_name)
        print("Location:", self.location)
        print("Total Beds:", self.total_beds)
        print("Contact Number:", self.contact_number)
        print("Specialization:", self.specialization)



hospital1 = Hospital("AIIMS Hospital", "New Delhi", 2500, "01126588500", "Multi-speciality")
hospital2 = Hospital("Civil Hospital", "Ahmedabad", 1200, "07922683721", "General Medicine")
hospital3 = Hospital("Kokilaben Hospital", "Mumbai", 750, "02242696969", "Multi-speciality")
hospital4 = Hospital("Sterling Hospital", "Rajkot", 300, "02812481111", "Cardiology")
hospital5 = Hospital("Apollo Hospital", "Chennai", 500, "04428293333", "Multi-speciality")



hospital1.display()
print("----------------------")

hospital2.display()
print("----------------------")

hospital3.display()
print("----------------------")

hospital4.display()
print("----------------------")

hospital5.display()