num_1 = int(input("Enter the First Number:"))
num_2 = int(input("Enter the Second Number:"))
num_3 = int(input("Enter the Third Number:"))

if num_1>num_2 and num_1>num_3:
    print("The Number 1 is larger!")
elif num_2>num_1 and num_2>num_3:
    print("The Number 2 is larger!")
else:
    print("The Number 3 is larger!")