from student import Student
from report import Report

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
        Teacher.all.append(self)

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