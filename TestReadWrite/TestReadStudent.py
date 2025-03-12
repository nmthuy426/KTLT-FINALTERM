from libs.JsonFileFactory import JsonFileFactory
from models.Student import Student

jff = JsonFileFactory()
filename = "../dataset/students.json"
students = jff.read_data(filename, Student)

print("sau khi đọc từ file:")
for s in students:
    print(s)