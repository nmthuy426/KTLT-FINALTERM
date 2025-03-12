from models.User import User

class Student(User):
    def __init__(self, user_id: str, fullname: str, birthday: str, gender: str, password: str,
                 student_class: str, major: str, course: str, advisor: str,
                 registered_classes=None, grades=None):  # 👈 Thêm tham số mặc định
        super().__init__(user_id, fullname, birthday, gender, password, "student")
        self.student_class = student_class
        self.major = major
        self.course = course
        self.advisor = advisor
        self.registered_classes = registered_classes if registered_classes is not None else []  # 👈 Xử lý mặc định
        self.grades = grades if grades is not None else {}  # 👈 Xử lý mặc định


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
            "Email": getattr(self, "email", "N/A"),  # Tránh lỗi nếu User không có email
            "Class": self.student_class,
            "Major": self.major,
            "Course": self.course,
            "Advisor": self.advisor
        }

    def __str__(self):
        return (
            f"Student ID: {self.user_id}, Name: {self.fullname}, Birthday: {self.birthday}, "
            f"Gender: {self.gender}, Email: {getattr(self, 'email', 'N/A')}, Class: {self.student_class}, "
            f"Major: {self.major}, Course: {self.course}, Advisor: {self.advisor},\n"
            f"Registered Classes: {', '.join(self.registered_classes) if self.registered_classes else 'None'}\n"
            f"Grades: {self.grades if self.grades else 'No grades recorded'}"
        )
