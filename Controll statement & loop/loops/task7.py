for i in range(1,51):
    if i % 2 == 0:
        if i % 3 == 0:
            print(f"{i} is divisible by both 2 and 3")
        else:
            print(f"{i} is divisbile by 2")
    elif i % 3 == 0:
        print(f"{i} is divisible by 3")
    else:
        print(f"{i} is not divisible by 2 or 3")    