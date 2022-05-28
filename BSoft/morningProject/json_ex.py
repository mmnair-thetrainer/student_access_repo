import json
import ast
import os


# os.mkdir("C:\\Users\\\shanu\\Documents\\pythonProject1\\CheckingFolder")


# CREATE NEW JSON FILE
def CreateJSONFile(student, fileLocation):
    filehandle = open(fileLocation, "w")
    filehandle.write(str(student))
    filehandle.close()


def readJsonFile(fileLocation):
    file_handle2 = open(fileLocation, "r")
    studentDetails = file_handle2.read()
    return studentDetails
    file_handle2.close()


def studentCRUD():
    Mode = input("enterC for CREATE, U for UPDATE, D for DELETE and R for READ").upper()
    students = {}
    rollNo = int(input("enter roll no"))
    FileLocation = str(rollNo) + ".json"
    if Mode == "C":
        name = input("enter name")
        age = input("enter age")
        contact = input("enter contact")
        try:
            eng = int(input("enter english marks"))
            mal = int(input("enter mal marks"))
            phy = int(input("enter phy marks"))
        except ValueError:
            print("Please enter a number")
        newStudent = {
            rollNo: {"name": name, "age": age, "contact": contact, "marks": {"eng": eng, "mal": mal, "phy": phy}}}
        students.update(newStudent)
        print(students)
        CreateJSONFile(students, FileLocation)
    elif Mode == "R":
        print(readJsonFile(FileLocation))
    elif Mode == "D":
        if os.path.exists(FileLocation):
            os.remove(FileLocation)
    elif Mode == "U":
        if os.path.exists(FileLocation):
            jsonString = readJsonFile(FileLocation)
            print(jsonString)
            #students = json.loads(jsonString)
            students = ast.literal_eval(json.dumps(jsonString))
            keyOfUpdate = input("enter what to change-name/age/contact/marks??").lower()
            newValue = input("enter new value")
            if keyOfUpdate in ("name", "age", "contact"):
                students[rollNo][keyOfUpdate] = newValue
                CreateJSONFile(students, FileLocation)
            elif keyOfUpdate == "marks":
                subject = input("enter subject code (eng/mal/phy)")
                if subject in ("eng", "mal", "phy"):
                    newMark = input("enter mark")
                    students[rollNo][keyOfUpdate][subject] = newMark
                    CreateJSONFile(students, FileLocation)
                else:
                    print("invalid subject code")
        else:
            print("Invalid Entry")
        print(students[rollNo])
    else:
        print("invalid entry")
        print(max(students.keys()))

while(1):
    studentCRUD()