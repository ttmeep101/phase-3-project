from models.__init__ import CURSOR, CONN

class Teacher:

    all = []

    def __init__(self, name, subject):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
        if isinstance(subject, str) and len(subject):
            self._subject = subject
        else:
            raise ValueError("Subject must be a non-empty string")

    def __repr__(self):
        return f"<Teacher(Name: {self.name}, Subject: {self.subject})>"

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
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, new_subject):
        if isinstance(new_subject, str) and len(new_subject):
            self._subject = new_subject
        else:
            raise ValueError("Subject must be a non-empty string")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            subject TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO teachers (name, subject)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.subject))
        CONN.commit()

        Teacher.all.append(self)

    @classmethod
    def create(cls, name, subject):
        teacher = cls(name, subject)
        teacher.save()
        return teacher
    
    def delete(self):
        sql = """
            DELETE FROM teachers
            WHERE name = ?
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        Teacher.all.remove(self)

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM teachers"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()

        teachers = []
        for row in rows:
            teacher = cls(row[1], row[2])  
            teachers.append(teacher)

        return teachers
    
    @classmethod
    def get_by_name(cls, name):
        sql = "SELECT * FROM teachers WHERE name = ?"
        CURSOR.execute(sql, (name,))
        rows = CURSOR.fetchall()

        teachers = []
        for row in rows:
            teacher = cls(row[1], row[2])
            teachers.append(teacher)

        return teachers
    
    @classmethod
    def get_by_subject(cls, subject):
        sql = "SELECT * FROM teachers WHERE subject = ?"
        CURSOR.execute(sql, (subject,))
        rows = CURSOR.fetchall()

        teachers = []
        for row in rows:
            teacher = cls(row[1], row[2])
            teachers.append(teacher)

        return teachers

    def get_id(self):
        sql = "SELECT id FROM teachers WHERE name = ?"
        CURSOR.execute(sql, (self.name,))
        result = CURSOR.fetchone()
        if result:
            return result[0]
        raise ValueError(f"Teacher {self.name} not found in the database.")
    
    @classmethod
    def load_all(cls):
        sql = "SELECT * FROM teachers"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        cls.all.clear()

        for row in rows:
            name = row[1]
            subject = row[2]
            teacher = cls(name, subject)
            cls.all.append(teacher)
