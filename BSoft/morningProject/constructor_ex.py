class ClassName:
    name = "Name"
    age = "21"
    gender = "f"
    course = "CS"
    def __init__(self, name):
        self.name = name

    def print_this(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.course)

obj2 = ClassName("Rekha")
obj2.print_this()
obj = ClassName("Shanooba")
print ("This is a line print")
obj.print_this()
