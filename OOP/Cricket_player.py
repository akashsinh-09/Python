class Cricket_player:

    def __init__(self, player_name, country, age, total_runs, role):
        self.player_name = player_name
        self.country = country
        self.age = age
        self.total_runs = total_runs
        self.role = role

    def display(self):

        print("Player Name:", self.player_name)
        print("Country:", self.country)
        print("Age:", self.age)
        print("Total Runs:", self.total_runs)
        print("Role:", self.role)


player1 = Cricket_player("Virat Kohli", "India", 38, 28000, "Batsman")
player2 = Cricket_player("Rohit Sharma", "India", 39, 19000, "Batsman")
player3 = Cricket_player("MS Dhoni", "India", 45, 17000, "Wicketkeeper")
player4 = Cricket_player("Ben Stokes", "England", 35, 7000, "All-rounder")
player5 = Cricket_player("Ken Wiiliamson", "New Zeland", 32, 14000, "Batsman")


player1.display()
print("----------------------")

player2.display()
print("----------------------")

player3.display()
print("----------------------")

player4.display()
print("----------------------")

player5.display()