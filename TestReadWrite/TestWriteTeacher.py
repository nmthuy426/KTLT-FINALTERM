from libs.JsonFileFactory import JsonFileFactory
from models.Student import Student
from models.Teacher import Teacher

teachers = []

teachers.append(Teacher("T001", "Nguyễn Văn A", "20/5/1980", "Male", "abc123", "Công nghệ thông tin", "K24401", ["Kinh tế vi mô", "Cấu trúc dữ liệu"]))
teachers.append(Teacher("T002", "Trần Thị B", "12/09/1985", "Female", "xyz789", "Kinh tế", "K24402", ["Lập trình Python", "Marketing căn bản"]))

print("Danh sách giáo viên:")
for e in teachers:
        print(e)
jff = JsonFileFactory()
filename = "../dataset/teachers.json"
jff.write_data(teachers, filename)
