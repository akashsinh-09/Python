def display_students(*args):
    
    if not args:
        print("No student names provided")
    else:
        for name in args:
            print(name)
    
display_students("Akash","Priyanshu","Venisha")