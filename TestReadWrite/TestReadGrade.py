from libs.JsonFileFactory import JsonFileFactory
from models.Grade import Grade

# Khởi tạo đối tượng JsonFileFactory
jff = JsonFileFactory()

# Đọc dữ liệu từ file JSON
filename = "../dataset/grades.json"
grades = jff.read_data(filename, Grade)

# In danh sách điểm sinh viên
print("📌 Danh sách điểm sinh viên đọc từ file:")
for g in grades:
    print(f"SV: {g.student_id} | Lớp: {g.class_id} | Điểm: {g.formative1}, {g.formative2}, {g.midterm}, {g.finalterm} | TB: {g.average}")