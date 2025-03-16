import json
from libs.JsonFileFactory import JsonFileFactory
from models.Teacher import Teacher
from models.Class import Class

# Tạo danh sách lớp học (dùng append)
classes = []
classes.append(Class("C001", "T001", "Phòng A101", "Thứ 2, 4, 6 (07:30 - 09:30)", "Lập trình Python", "Công nghệ thông tin", 20, 30))
classes.append(Class("C002", "T002", "Phòng B202", "Thứ 3, 5 (13:00 - 15:00)", "Kinh tế vi mô", "Kinh tế", 30, 50))
classes.append(Class("C003", "T001", "Phòng C303", "Thứ 2, 4 (09:30 - 11:30)", "Cấu trúc dữ liệu", "Công nghệ thông tin", 20, 40))
classes.append(Class("C004", "T002", "Phòng D404", "Thứ 7 (08:00 - 12:00)", "Marketing căn bản", "Kinh tế", 40, 60))

# In danh sách lớp học
print("📌 Danh sách lớp học:")
for c in classes:
    print(f"{c.class_id} - {c.subject} ({c.room}) - GV: {c.teacher} - Lịch học: {c.schedule}")

# Lưu vào file JSON
jff = JsonFileFactory()
filename = "../dataset/classes.json"
jff.write_data(classes, filename)