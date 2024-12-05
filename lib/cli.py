from functions import (
    create_tables,
    exit_program,
    add_teacher,
    display_teachers,
    remove_teacher,
    find_teacher_by_name,
    add_student,
    remove_student,
    display_students,
    find_teacher_by_subject,
    find_student_by_name,
    find_student_by_grade,
    find_student_by_teacher
)

def main():
    create_tables()
    while True:
        menu()
        choice = input("> ")
        if choice == '0':
            exit_program()
        elif choice == '1':
            add_teacher()
        elif choice == '2':
            remove_teacher()
        elif choice == '3':
            display_teachers()
        elif choice == '4':
            find_teacher_by_name()
        elif choice == '5':
            find_teacher_by_subject()
        elif choice == '6':
            add_student()
        elif choice == '7':
            remove_student()
        elif choice == '8':
            display_students()
        elif choice == '9':
            find_student_by_name()
        elif choice == '10':
            find_student_by_grade()
        elif choice == '11':
            find_student_by_teacher()
        else:
            print('Invalid input')

def menu():
    print("Please select an option:")
    print("0: Exit the application")
    print('1: Add a teacher')
    print('2: Remove a teacher')
    print('3: Display all teachers')
    print('4: Find teacher by name')
    print('5: Find teachers by subject')
    print('6: Add a student')
    print('7: Remove a student')
    print('8: Display all students')
    print('9: Find a student by name')
    print('10: Find students by grade level')
    print('11: Find students by teacher')

if __name__ == '__main__':
    main()