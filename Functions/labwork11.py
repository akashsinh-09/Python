def employee_data(**kwargs):

    required = ["name", "department", "salary"]

    for field in required:
        if field not in kwargs:
            print(f"This field is missing: {field}")
            return

    for key, value in kwargs.items():
        print(key, ":", value)


employee_data(name="Akash", department="I.T.", salary=30000)