from teacher import Teacher
from report import Report

class Student:

    all = []

    def __init__(self, name, grade, report, teacher):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
        if isinstance(grade, int) and grade >= 1 and grade <= 12:
            self._grade = grade
        else:
            raise ValueError("Grade must be a number between 1 and 12")
        if isinstance(report, Report):
            self._report = report
        else:
            raise ValueError("Report must be a valid Report object")
        if isinstance(teacher, Teacher):
            self._teacher = teacher
        else:
            raise ValueError("Teacher must be a valid Teacher object")
        Student.all.append(self)
    
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
    def report(self):
        return self._report

    @report.setter
    def report(self, new_report):
        if isinstance(new_report, Report):
            self._report = new_report
        else:
            raise ValueError("Report must be a valid Report object")
        
    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, new_teacher):
        if isinstance(new_teacher, Teacher):
            self._teacher = new_teacher
        else:
            raise ValueError("Teacher must be a valid Teacher object")