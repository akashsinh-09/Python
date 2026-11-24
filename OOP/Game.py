class Game:
    
    def __init__(self,game_name,game_type,developer,release_year,price):
        self.game_name = game_name
        self.game_type = game_type
        self.developer = developer
        self.release_year = release_year
        self.price = price
        
    def display(self):
        print("Game Name:",self.game_name)
        print("Game Type:",self.game_type)
        print("Developer:",self.developer)
        print("Relesed year:",self.release_year)
        print("Price:",self.price)
        
game1 = Game("GTA V", "Action-Adventure", "Rockstar Games", 2013, 1500)

game2 = Game("Minecraft", "Sandbox", "Mojang Studios", 2011, 999)

game3 = Game("PUBG", "Battle Royale", "Krafton", 2017, 0)

game4 = Game("FIFA 24", "Sports", "EA Sports", 2023, 2999)

game5 = Game("God of War", "Action", "Santa Monica Studio", 2018, 1999)

game1.display()
print()
game2.display()
print()
game3.display()
print()
game4.display()
print()
game5.display()