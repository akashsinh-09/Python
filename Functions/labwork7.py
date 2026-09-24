def display_students(*args):
    if not args:
        print("The name is not in the list!")
    else:
        for name in args:
            print("Student is:",name)
            
display_students("Akash","Priyanshu","Venisha")