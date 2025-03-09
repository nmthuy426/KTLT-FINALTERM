from models.User import User


class Teacher(User):
    def __init__(self, user_id: str, fullname: str, birthday: str, gender: str, password: str,
                 faculty: str, teacher_class: str):
        super().__init__(user_id, fullname, birthday, gender, password, "teacher")
        self.faculty = faculty  # Khoa của giáo viên
        self.teacher_class = teacher_class  # Lớp phụ trách
        self.assigned_classes = []

    def view_assigned_classes(self):
        return self.assigned_classes

    def enter_grades(self, classroom: 'Classroom', student_id: str, grade: float):
        if classroom.is_class_active():
            classroom.grades[student_id] = grade
            return f"✅ Grade entered for Student {student_id}: {grade}"
        return "⚠️ Class is not active yet."
