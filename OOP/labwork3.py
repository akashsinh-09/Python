class Grandparent:

    def grandparent_display(self):
        print("===== Grandparent Details =====")
        print("Name: Ramesh Patel")
        print("Role: Grandfather")
        print("Age: 75")


class Parent(Grandparent):

    def parent_display(self):
        print("\n===== Parent Details =====")
        print("Name: Suresh Patel")
        print("Role: Father")
        print("Age: 48")


class Child(Parent):

    def child_display(self):
        print("\n===== Child Details =====")
        print("Name: Rahul Patel")
        print("Role: Son")
        print("Age: 22")


child1 = Child()

child1.grandparent_display()
print()
child1.parent_display()
print()
child1.child_display()