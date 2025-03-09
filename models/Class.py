import json
from typing import List
from models.Teacher import Teacher
from models.Student import Student

class Classroom:
    def __init__(self, class_id: str, teacher: 'Teacher', room: str, schedule: str, subject: str, major: str, min_students: int, max_students: int):
        self.class_id = class_id
        self.teacher = teacher
        self.room = room
        self.schedule = schedule
        self.subject = subject
        self.major = major
        self.min_students = min_students
        self.max_students = max_students
        self.students = []
        self.grades = {}  # {student_id: grade}

    def add_student(self, student: 'Student'):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def is_class_active(self):
        return len(self.students) >= self.min_students