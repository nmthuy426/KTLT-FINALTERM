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

# Debug để kiểm tra danh sách giáo viên
print("DEBUG: Teachers Dictionary Loaded")
for k, v in teachers_dict.items():
    print(f"  {k} -> {v.fullname}")

# Khởi tạo JsonFileFactory
jff = JsonFileFactory()

# Đọc danh sách lớp học từ file JSON
filename = "../dataset/classes.json"
classes = jff.read_data(filename, Class, related_data={"teacher": teachers_dict})

# Kiểm tra nếu classes bị None hoặc rỗng
if not classes:
    print("❌ LỖI: Không đọc được dữ liệu lớp học! Kiểm tra lại JsonFileFactory hoặc file JSON.")
    exit()

# In danh sách lớp học sau khi đọc từ file
print("\n📌 Danh sách lớp học sau khi đọc từ file:")
for c in classes:
    teacher_name = c.teacher.fullname if c.teacher else "None"
    print(f"{c.class_id} - {c.subject} ({c.room}) - GV: {teacher_name} - Lịch học: {c.schedule}")
