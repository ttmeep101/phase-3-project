# from models.report import Report
# from models.student import Student
from models.teacher import Teacher

def exit_program():
    print('System closed')
    exit()

def add_teacher():
    tName = input("Enter a name: ")
    tSubject = input("Enter a subject: ")
    newTeacher = Teacher(tName, tSubject)
    print(f"New teacher added: {newTeacher} \n")

def remove_teacher():
    tName = input("Enter the name of the teacher you wish to remove:")
    for teacher in Teacher.all:
        if teacher.name == tName:
            Teacher.all.remove(teacher)
            print(f"Teacher {tName} has been removed. \n")
            return
    print(f"No teacher with the name {tName} has been found. \n")

def display_teachers():
    print(f"{Teacher.all} \n")

def test_teachers():
    testTeach1 = Teacher("Emma", "Math")
    testTeach2 = Teacher("Kevin", "Science")
    testTeach3 = Teacher("John", "Social Studies")