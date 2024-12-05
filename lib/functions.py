from models.student import Student
from models.teacher import Teacher

def exit_program():
    print('System closed')
    exit()

def add_teacher():
    tName = input("Enter a unique name: ")
    tSubject = input("Enter a subject: ")
    newTeacher = Teacher.create(tName, tSubject)
    print(f"New teacher added: {newTeacher} \n")

def remove_teacher():
    tName = input("Enter the name of the teacher you wish to remove:")
    for teacher in Teacher.all:
        if teacher.name.strip().lower() == tName.lower():
            teacher.delete()
            print(f"Teacher {tName} has been removed. \n")
            return
    print(f"No teacher with the name {tName} has been found. \n")

def display_teachers():
    teachers = Teacher.get_all()
    if not teachers:
        print("No teachers found. \n")
    else:
        for teacher in teachers:
            print(f"Name: {teacher.name}, Subject: {teacher.subject}")
        print()

def find_teacher_by_name():
    tName = input("Enter a name: ")
    checkName = Teacher.get_by_name(tName)
    if not checkName:
        print(f"No teachers with the name {tName} have been found. \n")
    else:
        for teacher in checkName:
            print(f"Name: {teacher.name}, Subject: {teacher.subject}")
        print()

def find_teacher_by_subject():
    tSubject = input("Enter a subject: ")
    checkSub = Teacher.get_by_subject(tSubject)
    if not checkSub:
        print(f"No teachers with the subject {tSubject} have been found. \n")
    else:
        for teacher in checkSub:
            print(f"Name: {teacher.name}, Subject: {teacher.subject}")
        print()
    

def add_student():
    sName = input("Enter a unique name: ")
    sGrade = input("Enter a grade level: ")
    sTeacher = input("Enter a teacher's name: ")
    teacher = Teacher.get_by_name(sTeacher)[0]
    newStudent = Student.create(sName, int(sGrade), teacher)
    print(f"New student added: {newStudent} \n")

def remove_student():
    sName = input("Enter the name of the student you wish to remove:")
    for student in Student.all:
        if student.name.strip().lower() == sName.lower():
            student.delete()
            print(f"Student {sName} has been removed. \n")
            return
    print(f"No student with the name {sName} has been found. \n")

def display_students():
    students = Student.get_all()
    if not students:
        print("No teachers found. \n")
    else:
        for student in students:
            print(f"Name: {student.name}, Grade: {student.grade}, Teacher: {student.teacher}")
        print()

def find_student_by_name():
    sName = input("Enter a name: ")
    student = Student.get_by_name(sName)
    if not student:
        print(f"No students with the name {sName} have been found. \n")
    else:
        print(f"Name: {student.name}, Grade: {student.grade}, Teacher: {student.teacher} \n")


def find_student_by_grade():
    sGrade = input("Enter a grade level: ")
    students = Student.get_by_grade(int(sGrade))
    if not students:
        print(f"No students were found in grade {int(sGrade)} \n")
    else:
        for student in students:
            print(f"Name: {student.name}, Grade: {student.grade}, Teacher: {student.teacher}")
        print()
    

def find_student_by_teacher():
    sTeacher = input("Enter a teacher's name: ")
    students = Student.get_by_teacher(sTeacher)
    if not students:
        print(f"No students were found in {sTeacher.name}'s class.")
    else:
        for student in students:
            print(f"Name: {student.name}, Grade: {student.grade}, Teacher: {student.teacher}")
        print()

def create_tables():
    Teacher.create_table()
    Student.create_table()
    Teacher.load_all()
    Student.load_all()
