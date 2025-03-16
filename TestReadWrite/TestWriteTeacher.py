from libs.JsonFileFactory import JsonFileFactory
from models.Student import Student
from models.Teacher import Teacher

teachers = []

teachers.append(Teacher("T001", "Nguyễn Văn A", "1980-05-20", "Male", "abc123", "Công nghệ thông tin", "K24401", ["Lập trình Python", "Cấu trúc dữ liệu"]))
teachers.append(Teacher("T002", "Trần Thị B", "1985-09-12", "Female", "xyz789", "Kinh tế", "K24402", ["Kinh tế vi mô", "Marketing căn bản"]))

print("Danh sách giáo viên:")
for e in teachers:
        print(e)
jff = JsonFileFactory()
filename = "../dataset/teachersjson"
jff.write_data(teachers, filename)
