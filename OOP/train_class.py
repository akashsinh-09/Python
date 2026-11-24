class Train:

    def __init__(self, train_number, train_name, source, destination, ticket_price):
        self.train_number = train_number
        self.train_name = train_name
        self.source = source
        self.destination = destination
        self.ticket_price = ticket_price

    def display(self):

        print("Train Number:", self.train_number)
        print("Train Name:", self.train_name)
        print("Source:", self.source)
        print("Destination:", self.destination)
        print("Ticket Price:", self.ticket_price)


train1 = Train(10101, "Rajdhani Express", "Mumbai", "Delhi", 2500)
train2 = Train(10202, "Shatabdi Express", "Ahmedabad", "Mumbai", 1500)
train3 = Train(10303, "Vande Bharat", "Rajkot", "Ahmedabad", 1200)
train4 = Train(10404, "Duronto Express", "Pune", "Delhi", 2000)
train5 = Train(10505, "Garib Rath", "Surat", "Mumbai", 800)


train1.display()
print("----------------------")

train2.display()
print("----------------------")

train3.display()
print("----------------------")

train4.display()
print("----------------------")

train5.display()