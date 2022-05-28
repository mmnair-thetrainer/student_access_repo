class Student:
    studentCount = 0 # data member

    def __init__(self, name, age): # constructor
        self.s_name = name
        self.s_age = age
        Student.studentCount += 1

    def _getCount(self): # member functions/ methods
        print("Total students ", Student.studentCount)

    def __getStudents(self):
        print("Name : ", self.s_name, "Age : ", self.s_age)

std1 = Student("Rekha","21") # instance/ object creation - instantiation
std1.getStudents()
std1.getCount()

del std1 #Desctructor
str(std1)

