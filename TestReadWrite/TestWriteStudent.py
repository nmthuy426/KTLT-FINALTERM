from libs.JsonFileFactory import JsonFileFactory
from models.Student import Student

students = []
students.append(Student("S001", "Nguyễn Văn A", "2004-01-15", "Male", "12345", "K24411", "Thương mại điện tử", "2024", "TS. Nguyễn Văn B"))
students.append(Student("S002", "Trần Thị B", "2004-02-20", "Female", "12345", "K24411E", "Thương mại điện tử", "2024", "TS. Lê Văn C"))
students.append(Student("S003", "Lê Văn C", "2004-03-10", "Male", "12345", "K24416", "AI và Trí tuệ nhân tạo", "2024", "TS. Phạm Văn D"))
students.append(Student("S004", "Phạm Thị D", "2004-04-30", "Female", "12345", "K24406", "Hệ thống thông tin quản lý", "2024", "TS. Nguyễn Thị E"))
students.append(Student("S005", "Hoàng Văn E", "2004-05-15", "Male", "12345", "K24411", "Thương mại điện tử", "2024", "TS. Trần Văn F"))
students.append(Student("S006", "Vũ Thị F", "2004-06-25", "Female", "12345", "K24411E", "Thương mại điện tử", "2024", "TS. Lê Thị G"))
students.append(Student("S007", "Đinh Văn G", "2004-07-12", "Male", "12345", "K24416", "AI và Trí tuệ nhân tạo", "2024", "TS. Phạm Văn H"))
students.append(Student("S008", "Ngô Thị H", "2004-08-05", "Female", "12345", "K24406", "Hệ thống thông tin quản lý", "2024", "TS. Nguyễn Văn I"))
students.append(Student("S009", "Bùi Văn I", "2004-09-18", "Male", "12345", "K24411", "Thương mại điện tử", "2024", "TS. Trần Thị J"))
students.append(Student("S010", "Tạ Thị J", "2004-10-22", "Female", "12345", "K24411E", "Thương mại điện tử", "2024", "TS. Hoàng Văn K"))
students.append(Student("S011", "Dương Văn K", "2004-11-14", "Male", "12345", "K24416", "AI và Trí tuệ nhân tạo", "2024", "TS. Lê Văn L"))
students.append(Student("S012", "Tống Thị L", "2004-12-19", "Female", "12345", "K24406", "Hệ thống thông tin quản lý", "2024", "TS. Phạm Văn M"))
students.append(Student("S013", "Chu Văn M", "2004-01-27", "Male", "12345", "K24411", "Thương mại điện tử", "2024", "TS. Nguyễn Thị N"))
students.append(Student("S014", "Phùng Thị N", "2004-02-28", "Female", "12345", "K24411E", "Thương mại điện tử", "2024", "TS. Trần Văn O"))
students.append(Student("S015", "Cao Văn O", "2004-03-09", "Male", "12345", "K24416", "AI và Trí tuệ nhân tạo", "2024", "TS. Lê Thị P"))
students.append(Student("S016", "Đoàn Thị P", "2004-04-25", "Female", "12345", "K24406", "Hệ thống thông tin quản lý", "2024", "TS. Hoàng Văn Q"))
students.append(Student("S017", "Hà Văn Q", "2004-05-30", "Male", "12345", "K24411", "Thương mại điện tử", "2024", "TS. Nguyễn Văn R"))
students.append(Student("S018", "Lương Thị R", "2004-06-10", "Female", "12345", "K24411E", "Thương mại điện tử", "2024", "TS. Phạm Văn S"))
students.append(Student("S019", "Tô Văn S", "2004-07-21", "Male", "12345", "K24416", "AI và Trí tuệ nhân tạo", "2024", "TS. Trần Thị T"))
students.append(Student("S020", "Giang Thị T", "2004-08-15", "Female", "12345", "K24406", "Hệ thống thông tin quản lý", "2024", "TS. Lê Văn U"))

print("Danh sách sinh viên:")
for s in students:
    print(s)

jff = JsonFileFactory()
filename = "../dataset/students.json"
jff.write_data(students, filename)