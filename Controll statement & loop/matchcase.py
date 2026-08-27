print("Press 1 to order a Sandwich")
print("Press 2 to order a Pizza")
print("Press 3 to order a Burger")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("You have ordered a Sandwich.")
        print("Press 1 for Veg Sandwich")
        print("Press 2 for Masala Sandwich")
        print("Press 3 for Cheese Sandwich")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                print("You have ordered a Veg Sandwich.")
            case 2:
                print("You have ordered a Masala Sandwich.")
            case 3:
                print("You have ordered a Cheese Sandwich.")
            case _:
                print("Invalid choice.")

    case 2:
        print("You have ordered a Pizza.")
        print("Press 1 for Veg Pizza")
        print("Press 2 for Corn Pizza")
        print("Press 3 for Cheese Pizza")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                print("You have ordered a Veg Pizza.")
            case 2:
                print("You have ordered a Corn Pizza.")
            case 3:
                print("You have ordered a Cheese Pizza.")
            case _:
                print("Invalid choice.")
    case 3:
        print("You have ordered a Burger.")
        print("Press 1 for Veg Burger")
        print("Press 2 for Masala Burger")
        print("Press 3 for Cheese Burger")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                print("You have ordered a Veg Burger.")
            case 2:
                print("You have ordered a Masala Burger.")
            case 3:
                print("You have ordered a Cheese Burger.")
            case _:
                print("Invalid choice.")
    case _:
        print("Invalid choice.")
        
           