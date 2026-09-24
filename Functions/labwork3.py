def square_list(numbers):
    return [num **2 for num in numbers]

values = list(map(int,input("Enter intergers seprated by space:").split()))

result = square_list(values)

print("Original List:",values)
print("Squared List:",result)