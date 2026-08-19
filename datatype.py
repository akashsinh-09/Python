print("Welcome to the Interactive Personal data collector! \n")

first_name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
favorite_number = int(input("Please enter your favorite number: \n"))

print("Thank you ! Here is the information we collected: \n")

print("Name:",first_name,type(first_name))
print("Age:",age,type(age))
print("Height:",height,type(height))
print("Favorite Number:",favorite_number,type(favorite_number),"\n\n")

print("Your birth year is approximately:", 2026 - age,"(based on the your age of",age,")\n")

print("Thank you for using the Personal Data Collector. Goodbye!")



