from libs.JsonFileFactory import JsonFileFactory
from models.Student import Student

students = []
students.append(Student("S001", "Lê Văn C", "10/03/2004", "Male", "12345", "K24416", "AI và Trí tuệ nhân tạo", "2024", "TS. Phạm Văn D"))
students.append(Student("S002", "Phạm Thị D", "30/04/2004", "Female", "12345", "K24406", "Hệ thống thông tin quản lý", "2024", "TS. Nguyễn Thị E"))
students.append(Student("S003", "Hoàng Văn E", "15/05/2004", "Male", "12345", "K24411", "Thương mại điện tử", "2024", "TS. Trần Văn F"))
students.append(Student("S004", "Vũ Thị F", "25/06/2004", "Female", "12345", "K24411E", "Thương mại điện tử", "2024", "TS. Lê Thị G"))
students.append(Student("S005", "Đinh Văn G", "12/07/2004", "Male", "12345", "K24416", "AI và Trí tuệ nhân tạo", "2024", "TS. Phạm Văn H"))
students.append(Student("S006", "Ngô Thị H", "05/08/2004", "Female", "12345", "K24406", "Hệ thống thông tin quản lý", "2024", "TS. Nguyễn Văn I"))
students.append(Student("S007", "Bùi Văn I", "18/09/2004", "Male", "12345", "K24411", "Thương mại điện tử", "2024", "TS. Trần Thị J"))
students.append(Student("S008", "Tạ Thị J", "22/10/2004", "Female", "12345", "K24411E", "Thương mại điện tử", "2024", "TS. Hoàng Văn K"))
students.append(Student("S009", "Dương Văn K", "14/11/2004", "Male", "12345", "K24416", "AI và Trí tuệ nhân tạo", "2024", "TS. Lê Văn L"))
students.append(Student("S010", "Tống Thị L", "19/12/2004", "Female", "12345", "K24406", "Hệ thống thông tin quản lý", "2024", "TS. Phạm Văn M"))
students.append(Student("S011", "Chu Văn M", "27/01/2004", "Male", "12345", "K24411", "Thương mại điện tử", "2024", "TS. Nguyễn Thị N"))
students.append(Student("S012", "Phùng Thị N", "28/02/2004", "Female", "12345", "K24411E", "Thương mại điện tử", "2024", "TS. Trần Văn O"))
students.append(Student("S013", "Cao Văn O", "09/03/2004", "Male", "12345", "K24416", "AI và Trí tuệ nhân tạo", "2024", "TS. Lê Thị P"))
students.append(Student("S014", "Đoàn Thị P", "25/04/2004", "Female", "12345", "K24406", "Hệ thống thông tin quản lý", "2024", "TS. Hoàng Văn Q"))
students.append(Student("S015", "Hà Văn Q", "30/05/2004", "Male", "12345", "K24411", "Thương mại điện tử", "2024", "TS. Nguyễn Văn R"))
students.append(Student("S016", "Lương Thị R", "10/06/2004", "Female", "12345", "K24411E", "Thương mại điện tử", "2024", "TS. Phạm Văn S"))
students.append(Student("S017", "Tô Văn S", "21/07/2004", "Male", "12345", "K24416", "AI và Trí tuệ nhân tạo", "2024", "TS. Trần Thị T"))
students.append(Student("S018", "Giang Thị T", "15/08/2004", "Female", "12345", "K24406", "Hệ thống thông tin quản lý", "2024", "TS. Lê Văn U"))

print("Danh sách sinh viên:")
for s in students:
    print(s)

jff = JsonFileFactory()
filename = "../dataset/students.json"
jff.write_data(students, filename)