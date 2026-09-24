def cube(num):
    return num ** 3

def calculate(numbers,operation):
    return[operation(n) for n in numbers]

numbers = list(map(int,input("Enter numbers:").split()))

result = calculate(numbers,cube)

print("Original List:",numbers)
print("Cube List:",result)