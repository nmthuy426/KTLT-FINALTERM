from models.User import User


class Teacher(User):
    def __init__(self, user_id: str, fullname: str, birthday: str, gender: str, password: str,
                 faculty: str, teacher_class: str,
                 assigned_classes=[],email=None):
        super().__init__(user_id, fullname, birthday, gender, password, "teacher")
        self.faculty = faculty  # Khoa của giáo viên
        self.teacher_class = teacher_class  # Lớp phụ trách
        self.assigned_classes = assigned_classes if assigned_classes is not None else []

    def view_assigned_classes(self):
        return self.assigned_classes

    def enter_grades(self, classroom: 'Classroom', student_id: str, grade: float):
        if classroom.is_class_active():
            classroom.grades[student_id] = grade
            return f"✅ Grade entered for Student {student_id}: {grade}"
        return "⚠️ Class is not active yet."

    def __str__(self):
        return f"Teacher ID: {self.user_id}, Name: {self.fullname},Email: {getattr(self, 'email', 'N/A')}, Birthday: {self.birthday}, Gender: {self.gender}, Faculty: {self.faculty}, Class: {self.teacher_class},\n Assigned Classes: {self.assigned_classes}"
