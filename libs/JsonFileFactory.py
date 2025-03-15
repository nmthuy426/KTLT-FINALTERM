import json
import os

from models.Student import Student
from models.Teacher import Teacher
from models.Class import Class


class JsonFileFactory:
    def write_data(self, arr_data, filename):
        """
        Hàm này dùng để parse object thành JSON string và ghi vào file.
        :param arr_data: Danh sách đối tượng
        :param filename: Đường dẫn file JSON
        :return: True nếu thành công
        """
        def serialize(obj):
            if isinstance(obj, Teacher) or isinstance(obj, Student):
                return obj.user_id  # Lưu user_id thay vì đối tượng
            return obj.__dict__  # Mặc định serialize object thành dict

        json_string = json.dumps(arr_data, default=serialize, indent=4, ensure_ascii=False)
        with open(filename, 'w', encoding='utf-8') as json_file:
            json_file.write(json_string)

    def read_data(self, filename, ClassName, related_data=None):
        """
        Đọc dữ liệu từ file JSON và ánh xạ các quan hệ.
        :param filename: Đường dẫn file JSON
        :param ClassName: Lớp đối tượng để parse dữ liệu vào
        :param related_data: Dictionary ánh xạ dữ liệu liên quan (VD: teachers_dict)
        :return: Danh sách đối tượng đã parse
        """
        if not os.path.isfile(filename):
            return []

        with open(filename, 'r', encoding='utf-8') as file:
            arr_data = json.load(file)

        # Kiểm tra related_data để tránh lỗi
        related_data = related_data or {}

        for obj in arr_data:
            # Nếu "teacher" là user_id, ánh xạ thành đối tượng Teacher
            if 'teacher' in obj and isinstance(obj['teacher'], str):
                obj['teacher'] = related_data.get(obj['teacher'], None)

            # Nếu "students" là danh sách user_id, ánh xạ thành danh sách Student
            if 'students' in obj and isinstance(obj['students'], list):
                obj['students'] = list(filter(None, [related_data.get(s_id, None) for s_id in obj['students']]))

        return [ClassName(**obj) for obj in arr_data]
