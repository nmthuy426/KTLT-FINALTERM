from models.Student import Student
from models.Teacher import Teacher
from models.Class import Class
from JsonFileFactory import JsonFileFactory


class DataConnector:
    def get_all_students(self):
        jff = JsonFileFactory()
        filename = "../dataset/students.json"
        students = jff.read_data(filename, Student)
        return students

    def get_all_teachers(self):
        jff = JsonFileFactory()
        filename = "../dataset/teachers.json"
        teachers = jff.read_data(filename, Teacher)
        return teachers

    def get_all_classrooms(self):
        jff = JsonFileFactory()
        filename = "../dataset/classrooms.json"
        classrooms = jff.read_data(filename, Class )
        return classrooms

    def login(self, username, password):
        # Kiểm tra trong danh sách sinh viên
        students = self.get_all_students()
        for student in students:
            if student.UserName == username and student.Password == password:
                return "student", student  # Phân quyền là student

        # Kiểm tra trong danh sách giáo viên
        teachers = self.get_all_teachers()
        for teacher in teachers:
            if teacher.UserName == username and teacher.Password == password:
                return "teacher", teacher  # Phân quyền là teacher

        return None, None
