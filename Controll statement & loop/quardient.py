x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

if x > 0 and y > 0:
    print(f"The coordinate point ({x},{y}) lies in the First quadrant.")
elif x < 0 and y > 0:
    print(f"The coordinate point ({x},{y}) lies in the Second quadrant.")
elif x < 0 and y < 0:
    print(f"The coordinate point ({x},{y}) lies in the Third quadrant.")
elif x > 0 and y < 0:
    print(f"The coordinate point ({x},{y}) lies in the Fourth quadrant.")
elif x == 0 and y == 0:
    print("The point lies at the Origin.")
elif x == 0:
    print("The point lies on the Y-axis.")
else:
    print("The point lies on the X-axis.")
