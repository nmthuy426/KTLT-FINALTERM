from libs.JsonFileFactory import JsonFileFactory
from models.Grade import Grade

# Tạo danh sách điểm (dùng append)
grades = []
grades.append(Grade("S001", "C001", 7, 8, 9, 10))
grades.append(Grade("S002", "C001", 6, 7, 8, 9))
grades.append(Grade("S003", "C002", 5, 6, 7, 8))
grades.append(Grade("S004", "C002", 8, 7, 9, 10))


for g in grades:
    print(g)
# Lưu vào file JSON
jff = JsonFileFactory()
filename = "../dataset/grades.json"
jff.write_data(grades, filename)
