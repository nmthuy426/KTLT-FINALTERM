from models.User import User


class Student(User):
    def __init__(self, user_id: str, fullname: str, birthday: str, gender: str, password: str,
                 student_class: str, major: str, course: str, advisor: str):
        super().__init__(user_id, fullname, birthday, gender, password,"student")
        self.student_class = student_class  # Lớp học của sinh viên
        self.major = major  # Ngành học
        self.course = course  # Khóa học (năm nhập học)
        self.advisor = advisor  # Cố vấn học tập
        self.registered_classes = []
        self.grades = {}  # Lưu điểm dưới dạng {class_id: điểm}

    def register_class(self, classroom: 'Classroom'):
        if classroom.add_student(self):
            self.registered_classes.append(classroom.class_id)
            return True
        return False

    def view_schedule(self):
        return self.registered_classes

    def view_grades(self):
        return self.grades

    def view_profile(self):
        return {
            "ID": self.user_id,
            "Full Name": self.fullname,
            "Birthday": self.birthday,
            "Gender": self.gender,
            "Email": self.email,
            "Class": self.student_class,
            "Major": self.major,
            "Course": self.course,
            "Advisor": self.advisor
        }
