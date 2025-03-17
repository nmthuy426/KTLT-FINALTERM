import json
import os


class JsonFileFactory:
    @staticmethod
    def write_data(arr_data, filename):
        """
        Ghi dữ liệu vào file JSON.
        :param arr_data: Danh sách đối tượng cần ghi.
        :param filename: Đường dẫn file.
        """
        if not isinstance(arr_data, list):
            raise ValueError("❌ Dữ liệu đầu vào phải là danh sách các đối tượng!")

        try:
            json_string = json.dumps(
                [obj.__dict__ for obj in arr_data if hasattr(obj, "__dict__")],
                default=str, indent=4, ensure_ascii=False
            )
            with open(filename, "w", encoding="utf-8") as json_file:
                json_file.write(json_string)
        except Exception as e:
            print(f"❌ Lỗi khi ghi file {filename}: {e}")

    @staticmethod
    def read_data(filename, ClassName, related_data=None):
        """
        Đọc dữ liệu từ file JSON và parse thành danh sách object.
        :param filename: Đường dẫn file JSON.
        :param ClassName: Class để parse dữ liệu.
        :param related_data: Dictionary ánh xạ dữ liệu liên quan.
        :return: Danh sách object.
        """
        if not os.path.isfile(filename):
            print(f"⚠️ Cảnh báo: File {filename} không tồn tại!")
            return []

        try:
            with open(filename, "r", encoding="utf-8") as file:
                arr_data = json.load(file)

            if not isinstance(arr_data, list):
                print(f"❌ Lỗi: Dữ liệu trong {filename} không phải là danh sách!")
                return []

            objects = []
            for obj in arr_data:
                if not isinstance(obj, dict):
                    continue  # Bỏ qua phần tử không phải dictionary

                # Ánh xạ dữ liệu liên quan (VD: teacher_id -> Teacher object)
                if related_data:
                    for key, mapping in related_data.items():
                        if key in obj and isinstance(obj[key], str):
                            obj[key] = mapping.get(obj[key], obj[key])  # Giữ nguyên nếu không tìm thấy

                # Tạo object từ dictionary
                try:
                    objects.append(ClassName(**obj))
                except TypeError as e:
                    print(f"⚠️ Lỗi khi khởi tạo {ClassName.__name__} với dữ liệu: {obj} -> {e}")

            return objects

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"❌ Lỗi khi đọc file {filename}: {e}")
            return []
