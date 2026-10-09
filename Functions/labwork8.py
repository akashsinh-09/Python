def filter_values(*args):
    
    strings = []
    numbers = []
    
    for value in args:
        
        
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