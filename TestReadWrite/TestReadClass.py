import json
from libs.JsonFileFactory import JsonFileFactory
from models.Class import Class

f = open('../dataset/teachers.json', 'r', encoding='utf-8')
teachers_data = json.load(f)
f.close()
#gán id qua fullname
teachers_dict = {}
for teacher in teachers_data:
    user_id = teacher['user_id']  # Lấy ID của giáo viên
    fullname = teacher['fullname']  # Lấy tên đầy đủ của giáo viên
    teachers_dict[user_id] = fullname  # Gán vào dictionary

classes = JsonFileFactory.read_data('../dataset/classes.json', Class, related_data={'teacher': teachers_dict})


# In danh sách lớp học
print("\n📌 Danh sách lớp học sau khi đọc từ file:")
for cls in classes:
    print(f"Class: {cls.class_id}, Subject: {cls.subject}, Teacher: {cls.teacher}, Room: {cls.room}, Schedule: {cls.schedule}")