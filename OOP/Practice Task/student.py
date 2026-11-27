class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        print("Name :",self.name)
        print("Age  :",self.age)
        
class Student(Person):
    
    def __init__(self, name, age,school,grade):
        super().__init__(name, age)
        self.school=school
        self.grade=grade
    
    def student_info(self):
        print("====Student Details====")
        self.introduce()
        print("School:",self.school)
        print("Grade:",self.grade)
        
s1=Student("Akash",21,"XYZ","A")

s1.student_info()