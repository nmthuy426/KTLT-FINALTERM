import json
from libs.JsonFileFactory import JsonFileFactory
from models.Class import Class

# Đọc dữ liệu từ file JSON
jff = JsonFileFactory()
filename = "../dataset/classes.json"

# Đọc dữ liệu lớp học từ file
classes_data = jff.read_data(filename, Class)

# In danh sách lớp học từ file
print("📌 Danh sách lớp học đọc từ file:")
for c in classes_data:
    print(f"{c.class_id} - {c.subject} ({c.room}) - GV: {c.teacher} - Lịch học: {c.schedule}")
