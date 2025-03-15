from typing import List
from models.Teacher import Teacher
from models.Student import Student

class Class:
    def __init__(self, class_id: str, teacher: Teacher, room: str, schedule: str, subject: str, major: str,
                 min_students: int, max_students: int, students: List[Student] = None, grades=None):
        self.class_id = class_id
        self.teacher = teacher if isinstance(teacher, Teacher) else None
        self.room = room
        self.schedule = schedule
        self.subject = subject
        self.major = major
        self.min_students = min_students
        self.max_students = max_students
        self.students = students if students else []
        self.grades = grades if grades else {}

    def add_student(self, student: Student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def is_class_active(self):
        return len(self.students) >= self.min_students

    def __str__(self):
        teacher_name = self.teacher.fullname if self.teacher else "Unknown"
        student_list = ", ".join([s.fullname for s in self.students]) if self.students else "None"
        grade_list = ", ".join([f"{s}: {g}" for s, g in self.grades.items()]) if self.grades else "None"

        return (f"Class ID: {self.class_id}, Teacher: {teacher_name}, Room: {self.room}, "
                f"Schedule: {self.schedule}, Subject: {self.subject}, Major: {self.major}, "
                f"Min Students: {self.min_students}, Max Students: {self.max_students}, "
                f"Students ({len(self.students)}/{self.max_students}): {student_list}, Grades: {grade_list}")

    def __repr__(self):
        """ Hàm này sẽ được dùng khi in danh sách lớp học """
        return f"{self.class_id} - {self.subject} ({self.room}) - GV: {self.teacher.fullname if self.teacher else 'None'} - Lịch học: {self.schedule}"
