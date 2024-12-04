
from functions import (
    test_teachers,
    exit_program,
    add_teacher,
    display_teachers,
    remove_teacher
)

def main():
    test_teachers()
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
        else:
            print('Invalid input')

def menu():
    print("Please select an option:")
    print("0: Exit the application")
    print('1: Add a teacher')
    print('2: Remove a teacher')
    print('3: Display all teachers')

if __name__ == '__main__':
    main()