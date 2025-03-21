import json
from libs.JsonFileFactory import JsonFileFactory
from models.Grade import Grade

# Tạo danh sách điểm (dùng append)
grades = []
grades.append(Grade("S001", "C001", 7, 8, 9, 10))
grades.append(Grade("S002", "C001", 6, 7, 8, 9))
grades.append(Grade("S003", "C002", 5, 6, 7, 8))
grades.append(Grade("S004", "C002", 8, 7, 9, 10))

# In danh sách điểm
print("📌 Danh sách điểm sinh viên:")
for g in grades:
    print(f"SV: {g.student_id} | Lớp: {g.class_id} | Điểm: {g.formative1}, {g.formative2}, {g.midterm}, {g.finalterm} | TB: {g.average}")

# Lưu vào file JSON
jff = JsonFileFactory()
filename = "../dataset/grades.json"
jff.write_data([g.to_dict() for g in grades], filename)

print("✅ Dữ liệu điểm đã được ghi vào 'dataset/grades.json'.")
