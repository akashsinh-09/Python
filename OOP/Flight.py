class Flight:

    def __init__(self, flight_number, airline_name, source, destination, ticket_price):
        self.flight_number = flight_number
        self.airline_name = airline_name
        self.source = source
        self.destination = destination
        self.ticket_price = ticket_price

    def display(self):

        print("Flight Number:", self.flight_number)
        print("Airline Name:", self.airline_name)
        print("Source:", self.source)
        print("Destination:", self.destination)
        print("Ticket Price:", self.ticket_price)


flight1 = Flight("AI101", "Air India", "Ahmedabad", "Delhi", 5500)
flight2 = Flight("6E202", "IndiGo", "Mumbai", "Bangalore", 4200)
flight3 = Flight("UK303", "Vistara", "Delhi", "Goa", 6500)
flight4 = Flight("SG404", "SpiceJet", "Surat", "Hyderabad", 4800)
flight5 = Flight("QP505", "Akasa Air", "Ahmedabad", "Mumbai", 3500)


flight1.display()
print("----------------------")

flight2.display()
print("----------------------")

flight3.display()
print("----------------------")

flight4.display()
print("----------------------")

flight5.display()