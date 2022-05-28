class Student:
    name = "Manu" #Member Variable

    def __init__(self, name): #Constructor
        print("Constructor invoked ", name)

ins = Student(input("Enter name: "))
