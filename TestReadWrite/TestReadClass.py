import json
from libs.JsonFileFactory import JsonFileFactory
from models.Teacher import Teacher
from models.Class import Class

# Đọc danh sách giáo viên từ file JSON
teachers_dict = {}
with open("../dataset/teachers.json", "r", encoding="utf-8") as file:
    teacher_data = json.load(file)
    for t in teacher_data:
        teacher = Teacher(
            t["user_id"], t["fullname"], t["birthday"], t["gender"],
            t["password"], t["faculty"], t["teacher_class"], t["assigned_classes"]
        )
        teachers_dict[t["user_id"]] = teacher  # Lưu vào dictionary theo user_id

# Khởi tạo JsonFileFactory
jff = JsonFileFactory()

# Đọc danh sách lớp học từ file JSON và ánh xạ teachers
filename = "../dataset/classes.json"
classes = jff.read_data(filename, Class, teachers_dict)

# In danh sách lớp học sau khi đọc từ file
print("📌 Danh sách lớp học sau khi đọc từ file:")
for c in classes:
    teacher_names = ", ".join([t.fullname for t in c.teacher]) if c.teacher else "None"
    print(f"{c.class_id} - {c.subject} ({c.room}) - GV: {teacher_names} - Lịch học: {c.schedule}")
