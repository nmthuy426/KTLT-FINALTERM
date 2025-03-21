import json
from libs.JsonFileFactory import JsonFileFactory
from models.Class import Class
from TestReadWrite.TestWriteTeacher import Teacher  # Sửa đường dẫn nếu cần

# Đọc dữ liệu giáo viên từ file teachers.json
f = open('../dataset/teachers.json', 'r', encoding='utf-8')
teachers_data = json.load(f)
f.close()

# Đọc dữ liệu lớp học từ file classes.json và ánh xạ thông tin giáo viên
jff = JsonFileFactory()
classes = jff.read_data('../dataset/classes.json', Class)

# In danh sách lớp học
print("\n📌 Danh sách lớp học sau khi đọc từ file:")
for cls in classes:
    print(f"Class: {cls.class_id}, Subject: {cls.subject}, Teacher: {cls.teacher}, Room: {cls.room}, Schedule: {cls.schedule}")
