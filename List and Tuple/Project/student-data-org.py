

print("Welcome to the Student Data Organization!")
students = []

while True:
    print("\nPlease choose an option:")
    print("1. Add a new student")
    print("2. Display all students")
    print("3. Update a student's information")
    print("4. Delete a student")
    print("5. Display Subject offered")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    match choice:
        case "1":
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            age = int(input("Enter student age: ")) 
            grade = input("Enter student grade: ")
            dob = input("Enter student date of birth (YYYY-MM-DD): ")
            subjects = set(input("Enter subjects offered (comma-separated): ").split(","))
            
            student_identity = (student_id,dob)
            
            student = {
                "identity": student_identity,
                "name": name,
                "age": age,
                "grade": grade,
                "dob": dob,
                "subjects": subjects
            }
            students.append(student)
            print("\nStudent added successfully!")
            
        case "2":
            if not students:
                print("No students found.")
            else:
                print("\nList of Students:")
                for student in students:
                    print(f"ID: {student['identity'][0]}, Name:{student['name']},Age: {student['age']}, Grade: {student['grade']}, Subjects: {', '.join(student['subjects'])}")
        case "3":
            student_id = int(input("Enter the student ID to update: "))
            for student in students:
                if student['identity'][0] == student_id:
                    name = input("Enter new name: ")
                    age = int(input("Enter new age: "))
                    grade = input("Enter new grade: ")
                    dob = input("Enter new date of birth (YYYY-MM-DD): ")
                    subjects = set(input("Enter new subjects offered (comma-separated): ").split(","))
                    student.update({
                        "name": name,
                        "age": age,
                        "grade": grade,
                        "dob": dob,
                        "subjects": subjects
                    })
                    print("\nStudent information updated successfully!")
                    break
            else:
                print("Student not found.")