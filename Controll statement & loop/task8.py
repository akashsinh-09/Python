value_1 = int(input("Enter a value of 1 side:"))
value_2 = int(input("Enter a value of 2 side:"))
value_3 = int(input("Enter a value of 3 side:"))

total = value_1+value_2+value_3

if total == 180:
    print("This is Triangel!")
else:
    print("The values are not match!")