from TestReadWrite.TestWriteTeacher import Teacher
from libs.JsonFileFactory import JsonFileFactory
# Dữ liệu sinh viên mẫu
jff=JsonFileFactory()
filename= "../dataset/teachers.json"
eas=jff.read_data(filename,Teacher)
for e in eas:
   print(e)