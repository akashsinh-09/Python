age = int(input("Enter your age:"))

if age >= 0 and age <=12:
    print("This is child age!")
elif age >=13 and age <=19:
    print("This is Teenager age!")
elif age >=20 and age <=59:
    print("This is Adult age!")
else:
    print("This is senior age!")