def filter_values(*args):
<<<<<<< HEAD
    
=======
>>>>>>> 414a7741cda9aef7d3c866982c2babb40850b553
    strings = []
    numbers = []
    
    for value in args:
<<<<<<< HEAD
        
        
        if type(value) == str:
            strings.append(value)
            print("The value is String:",value)
        elif type(value) == int:
            numbers.append(value)
            print("The value is Number:",value)
        else:  
            print("The value is not in the list")
        
    
    return tuple(strings), tuple(numbers)
    
filter_values("Akash",20,"Python",35,"BMW",3.14)
=======
        if type(value) == str:
            strings.append(value)
        elif type(value) == int:
            numbers.append(value)
    return tuple(strings), tuple(numbers)


s, n = filter_values("Akash", 20, "Python", 35, "Rajkot")

print("Strings:", s)
print("Numbers:", n)
>>>>>>> 414a7741cda9aef7d3c866982c2babb40850b553
