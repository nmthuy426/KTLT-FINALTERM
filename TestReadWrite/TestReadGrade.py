from libs.JsonFileFactory import JsonFileFactory
from models.Grade import Grade
jff = JsonFileFactory()
filename = "../dataset/grades.json"
grades = jff.read_data(filename, Grade)

print("sau khi đọc từ file:")
for g in grades:
    print(g)