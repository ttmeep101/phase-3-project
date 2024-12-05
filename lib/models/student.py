from models.teacher import Teacher
from models.__init__ import CONN, CURSOR 

class Student:

    all = []

    def __init__(self, name, grade, teacher):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
        if isinstance(grade, int) and grade >= 1 and grade <= 12:
            self._grade = grade
        else:
            raise ValueError("Grade must be a number between 1 and 12")
        if isinstance(teacher, Teacher):
            self._teacher = teacher
        else:
            raise ValueError("Teacher must be a valid Teacher object")
    
    def __repr__(self):
        return f"<Student(Name: {self.name}, Grade: {self.grade}, Teacher: {self.teacher})>"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name):
            self._name = new_name
        else:
            raise ValueError("Name must be a non-empty string")
    
    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        if isinstance(new_grade, int) and new_grade >= 1 and new_grade <= 12:
            self._grade = new_grade
        else:
            raise ValueError("Grade must be a number between 1 and 12")
        
    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, new_teacher):
        if isinstance(new_teacher, Teacher):
            self._teacher = new_teacher
        else:
            raise ValueError("Teacher must be a valid Teacher object")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            grade INTEGER,
            teacher_id INTEGER,
            FOREIGN KEY (teacher_id) REFERENCES teachers(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO students (name, grade, teacher_id)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.grade, self.teacher.get_id()))
        CONN.commit()

        Student.all.append(self)

    @classmethod
    def create(cls, name, grade, teacher):
        student = cls(name, grade, teacher)
        student.save()
        return student
    
    def delete(self):
        sql = """
            DELETE FROM students
            WHERE name = ?
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        Student.all.remove(self)

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM students"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()

        students = []
        for row in rows:
            name = row[1]
            grade = row[2]
            teacher_id = row[3]

            CURSOR.execute("SELECT * FROM teachers WHERE id = ?", (teacher_id,))
            teacher_row = CURSOR.fetchone()
            if teacher_row:
                teacher = Teacher(teacher_row[1], teacher_row[2])
            else:
                teacher = None

            student = cls(name, grade, teacher)
            students.append(student)

        return students
    
    @classmethod
    def get_by_name(cls, name):
        sql = """
            SELECT * FROM students
            WHERE name = ?
        """
        CURSOR.execute(sql, (name,))
        row = CURSOR.fetchone()

        if row:
            student_name = row[1]
            grade = row[2]
            teacher_id = row[3]

            CURSOR.execute("SELECT * FROM teachers WHERE id = ?", (teacher_id,))
            teacher_row = CURSOR.fetchone()

            if teacher_row:
                teacher = Teacher(teacher_row[1], teacher_row[2])
            else:
                teacher = None

            return cls(student_name, grade, teacher)
        else:
            return None
        
    @classmethod
    def get_by_grade(cls, grade):
        sql = """
        SELECT * FROM students
        WHERE grade = ?
        """
        CURSOR.execute(sql, (grade,))
        rows = CURSOR.fetchall()

        students = []
        for row in rows:
            name = row[1]
            grade = row[2]
            teacher_id = row[3]

            CURSOR.execute("SELECT * FROM teachers WHERE id = ?", (teacher_id,))
            teacher_row = CURSOR.fetchone()
            
            if teacher_row:
                teacher = Teacher(teacher_row[1], teacher_row[2])
            else:
                teacher = None

            student = cls(name, grade, teacher)
            students.append(student)
        return students
    
    @classmethod
    def get_by_teacher(cls, teacher_name):
        sql_teacher = """
        SELECT * FROM teachers
        WHERE name = ?
        """
        CURSOR.execute(sql_teacher, (teacher_name,))
        teacher_row = CURSOR.fetchone()

        if not teacher_row:
            return []
        
        teacher_id = teacher_row[0]
        teacher_subject = teacher_row[1]
        teacher = Teacher(teacher_name, teacher_subject)

        sql_students = """
        SELECT * FROM students
            WHERE teacher_id = ?
        """
        CURSOR.execute(sql_students, (teacher_id,))
        student_rows = CURSOR.fetchall()

        students = []
        for row in student_rows:
            student_name = row[1]
            grade = row[2]
            students.append(cls(student_name, grade, teacher))

        return students
    
    @classmethod
    def load_all(cls):
        sql = "SELECT * FROM students"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        cls.all.clear()

        for row in rows:
            name = row[1]
            grade = row[2]
            teacher_id = row[3]
            teacher = next((t for t in Teacher.all if getattr(t, 'id', None) == teacher_id), None)
            if teacher:
                student = cls(name, grade, teacher)
                cls.all.append(student)