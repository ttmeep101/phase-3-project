# School Management CLI
A simple program that can be used to both enter and store information on teachers and students within a school system.

## How to Use:
When the program starts, a menu will appear with multiple options choose from. Entering a number will pull up that function and give prompts to the user to help display data. Below are detailed descriptions of what each function does and requires, as invalid inputs will return an error explaining what was wrong with the input.

Running the command python lib/cli.py will start the program.

## Different Functions:
0. Exiting the application - simply exits the application easily instead of forcefully exiting
1. Adding a teacher - it will prompt the user for a UNIQUE name (string) and a subject (string) to assign to the newly created teacher
2. Remove a teacher - will prompt the user for the name of a teacher, which will remove the teacher from the database
3. Display all teachers - will print a list of all currently stored teachers
4. Find teacher by name - will prompt the user for a name that will return the teacher with that name
5. Find teacher by subject - will prompt the user for a subject that will return any teachers teaching that subject
6. Add a student - will prompt the user for a UNIQUE name (string), grade level (number), and a teacher that the student is assigned too, using the teacher's name
7. Remove a student - will prompt the user for a student's name, and will remove the given student from the database
8. Display all students - will print a list of all currently stored students
9. Find student by name - will prompt the user for the name of a student, and return the given student
10. Find student by grade level - will prompt the user for a grade level number, and return all students in that grade level
11. Find students by teacher = will prompt the user for the name of a teacher, and return all students that are tought by the given teacher