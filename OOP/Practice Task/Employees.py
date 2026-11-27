class Employee:
    def __init__(self,name,employee_id,basic_salary):
        self.name =name
        self.emp_id=employee_id
        self.salary=basic_salary
        
    def show_employee(self):
        print("======Employee Details======")
        print()
        print("Employee Name:",self.name)
        print("Employee ID  :",self.emp_id)
        print("Basic Salary :",self.salary)
        
class Manager(Employee):
    def __init__(self, name, employee_id, basic_salary,department):
        super().__init__(name, employee_id, basic_salary)
        self.department=department
        
    def show_manager(self):
        self.show_employee()
        print("Department :",self.department)
        
class SeniorManger(Manager):
    def __init__(self, name, employee_id, basic_salary, department,bonus):
        super().__init__(name, employee_id, basic_salary, department)
        self.bonus=bonus
        
    def calcultae_total_salary(self):
        total_salary=self.salary + self.bonus
        self.show_manager()
        print("Total Salary:",total_salary)

emp1=SeniorManger("Akash",1234,25000,"Data",5000)

emp1.calcultae_total_salary()