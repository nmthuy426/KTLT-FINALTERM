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

# Tạo danh sách lớp học (dùng append)
classes = []
classes.append(Class("C001", teachers_dict["T001"], "Phòng A101", "Thứ 2, 4, 6 (07:30 - 09:30)", "Lập trình Python", "Công nghệ thông tin", 20, 30))
classes.append(Class("C002", teachers_dict["T002"], "Phòng B202", "Thứ 3, 5 (13:00 - 15:00)", "Kinh tế vi mô", "Kinh tế", 30, 50))
classes.append(Class("C003", teachers_dict["T001"], "Phòng C303", "Thứ 2, 4 (09:30 - 11:30)", "Cấu trúc dữ liệu", "Công nghệ thông tin", 20, 40))
classes.append(Class("C004", teachers_dict["T002"], "Phòng D404", "Thứ 7 (08:00 - 12:00)", "Marketing căn bản", "Kinh tế", 40, 60))

# In danh sách lớp học
print("📌 Danh sách lớp học:")
for c in classes:
    print(f"{c.class_id} - {c.subject} ({c.room}) - GV: {c.teacher.fullname} - Lịch học: {c.schedule}")

# Lưu vào file JSON
jff = JsonFileFactory()
filename = "../dataset/classes.json"
jff.write_data(classes, filename)