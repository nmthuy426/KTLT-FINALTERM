class Admin:
    def __init__(self):
        self.students = []  # Danh sách Student
        self.teachers = []  # Danh sách Teacher
        self.classrooms = []

    def create_user(self, user_type: str, user_id: str, fullname: str, birthday: str, gender: str, email: str, password: str):
        if user_type == "student":
            user = Student(user_id, fullname, birthday, gender, email, password)
            self.students.append(user)
        elif user_type == "teacher":
            user = Teacher(user_id, fullname, birthday, gender, email, password)
            self.teachers.append(user)
        else:
            print(f"❌ Error: Invalid user type '{user_type}'")
            return None
        return user

    def create_classroom(self, class_id: str, teacher: 'Teacher', room: str, schedule: str, subject: str, major: str, min_students: int, max_students: int):
        classroom = Classroom(class_id, teacher, room, schedule, subject, major, min_students, max_students)
        self.classrooms.append(classroom)
        teacher.assigned_classes.append(class_id)
        return classroom