import random

mylist = ["Rock", "Paper", "Scissors"]
print("Rock")
print("Paper")
print("Scissors")
total_life = 5

while True:
    computer_choice = mylist[int(random.random() * 3)]
    
    user_choice = input("Enter your choice: ")
    total_life -= 1
    
    if(user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Scissors" and computer_choice == "Paper"):
        print("You win!")
    elif(computer_choice  == "Rock" and user_choice == "Scissors") or (computer_choice == "Paper" and user_choice == "Rock") or (computer_choice == "Scissors" and user_choice == "Paper"):
        print("You lose!")
    elif(user_choice == computer_choice):
        print("It's a tie!")
    elif(user_choice not in mylist):
        print("Invalid input. Please choose Rock, Paper, or Scissors.")
    elif(total_life == 0):
        print("Game Over! You have no more lives left.")
        break