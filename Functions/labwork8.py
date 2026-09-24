def filter_values(*args):
    strings = []
    numbers = []
    
    for value in args:
        if type(value) == str:
            strings.append(value)
        elif type(value) == int:
            numbers.append(value)
    return tuple(strings), tuple(numbers)


s, n = filter_values("Akash", 20, "Python", 35, "Rajkot")

print("Strings:", s)
print("Numbers:", n)