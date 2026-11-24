class Football_player:

    def __init__(self, player_name, age, country, position, jersey_number):
        self.player_name = player_name
        self.age = age
        self.country = country
        self.position = position
        self.jersey_number = jersey_number

    def display(self):

        print("Player Name:", self.player_name)
        print("Age:", self.age)
        print("Country:", self.country)
        print("Position:", self.position)
        print("Jersey Number:", self.jersey_number)


player1 = Football_player("Lionel Messi", 39, "Argentina", "Forward", 10)
player2 = Football_player("Cristiano Ronaldo", 41, "Portugal", "Forward", 7)
player3 = Football_player("Neymar Jr", 34, "Brazil", "Forward", 10)
player4 = Football_player("Luka Modric", 41, "Croatia", "Midfielder", 10)
player5 = Football_player("Virgil van Dijk", 35, "Netherlands", "Defender", 4)


player1.display()
print("----------------------")

player2.display()
print("----------------------")

player3.display()
print("----------------------")

player4.display()
print("----------------------")

player5.display()