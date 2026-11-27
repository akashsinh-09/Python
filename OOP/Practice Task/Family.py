class GrandFather:
    def __init__(self,grandfather_name,family_name):
        self.grandfather=grandfather_name
        self.family=family_name
    
    def grandfather_info(self):
        print("GrandFather Name:",self.grandfather)
        print("Family          :",self.family)
        
class Father(GrandFather):
    def __init__(self, grandfather_name, family_name,father_name):
        super().__init__(grandfather_name, family_name)
        self.fathername=father_name
    
    def father_info(self):
        self.grandfather_info()
        print("Father Name     :",self.fathername)
        
class Child(Father):
    def __init__(self, grandfather_name, family_name, father_name,child_name):
        super().__init__(grandfather_name, family_name, father_name)
        self.childname=child_name
        
    def family_tree(self):
        self.father_info()
        print("Child Name      :",self.childname)
        
child1=Child("Shivubha","Sodha","Narendrasinh","Akashsinh")

child1.family_tree()