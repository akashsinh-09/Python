number = input("Enter a number: ")
print("The type of the number is:",type(number)) 

print("\nAfter the type casting:")
num = int(number)
print("The number is:",num)
print("The type of the number is:",type(num)) 

num = float(number)
print("The number is:",num,type(num))

num = bool(number)
print("The number is:",num,type(num))