def person_description(**kwargs):
    print("Person Details")

    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")


person_description(
    name="Akash",
    age=20,
    city="Rajkot"
)