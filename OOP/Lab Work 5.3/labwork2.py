class Teacher:
    def teacher_details(self):
        print("Teacher Details")
        print("Subject:Python")
        print("Expression: 5 years")
        
class Administrator:
    def admin_details(self):
        print("Administrator Details")
        print("Department: Accedamic")
        print("Role: Administrator")
        
class Headmaster(Teacher,Administrator):
    def headmaster_details(self):
        print("Headmaster Details")
        print("Name :Akashsinh Sodha")
        print("Position: Headmaster")
        
headmaster1=Headmaster()

headmaster1.headmaster_details()
print()
headmaster1.teacher_details()
print()
headmaster1.admin_details()