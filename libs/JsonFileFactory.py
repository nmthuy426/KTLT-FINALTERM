import json
import os


class JsonFileFactory:
    @staticmethod
    def write_data(arr_data, filename):
        """
        Ghi dữ liệu vào file JSON
        :param arr_data: Mảng đối tượng
        :param filename: Tên file
        """
        json_string = json.dumps([item.__dict__ for item in arr_data], default=str, indent=4, ensure_ascii=False)
        with open(filename, 'w', encoding='utf-8') as json_file:
            json_file.write(json_string)

    @staticmethod

    def read_data(filename, ClassName, related_data=None):
        """
        Đọc dữ liệu từ file JSON và parse thành object
        :param filename: Tên file
        :param ClassName: Class để parse dữ liệu
        :param related_data: Dữ liệu liên quan để ánh xạ
        :return: Mảng object
        """
        if not os.path.isfile(filename):
            return []
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                arr_data = json.load(file)

            # Ánh xạ dữ liệu liên quan (ví dụ: ánh xạ teacher từ teachers.json vào classes.json)
            for obj in arr_data:
                for key, mapping in (related_data or {}).items():
                    if key in obj:
                        obj[key] = mapping.get(obj[key], obj[key])

            return [ClassName(**obj) for obj in arr_data]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"❌ Lỗi khi đọc file {filename}: {e}")
            return []