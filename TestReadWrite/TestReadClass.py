import json
from libs.JsonFileFactory import JsonFileFactory
from models.Class import Class
from TestReadWrite.TestWriteTeacher import Teacher  # Sửa đường dẫn nếu cần

# Đọc dữ liệu giáo viên từ file teachers.json
f = open('../dataset/teachers.json', 'r', encoding='utf-8')
teachers_data = json.load(f)
f.close()

# Tạo dictionary để ánh xạ từ fullname sang user_id
teachers_dict = {}
for teacher in teachers_data:
    user_id = teacher['user_id']  # Lấy ID của giáo viên
    fullname = teacher['fullname']  # Lấy tên đầy đủ của giáo viên
    teachers_dict[fullname] = user_id  # Gán fullname làm key, user_id làm value

# Đọc dữ liệu lớp học từ file classes.json và ánh xạ thông tin giáo viên
jff = JsonFileFactory()
classes = jff.read_data('../dataset/classes.json', Class, related_data={'teacher': teachers_dict})

# In danh sách lớp học
print("\n📌 Danh sách lớp học sau khi đọc từ file:")
for cls in classes:
    print(f"Class: {cls.class_id}, Subject: {cls.subject}, Teacher ID: {cls.teacher}, Room: {cls.room}, Schedule: {cls.schedule}")

# Nếu muốn làm việc với dữ liệu sinh viên, có thể sử dụng mã dưới đây:
filename = "../dataset/teachers.json"
students = jff.read_data(filename, Teacher)
