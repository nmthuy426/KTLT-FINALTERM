from TestReadWrite.TestWriteTeacher import Teacher
from libs.JsonFileFactory import JsonFileFactory
from models.Student import Student
# Dữ liệu sinh viên mẫu
jff=JsonFileFactory()
filename= "../dataset/Teacher.json"
eas=jff.read_data(filename,Student)
for e in eas:
   print(e)