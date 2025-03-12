import json
import os

from models.Student import Student


class JsonFileFactory:
    def write_data(self,arr_data,filename):
        """
        Hàm này dùng để parse object thành jsonstring
        :param arr_data: mảng đối tượng
        :param filename:nơi lưu trữ jsonstring cho object
        :return: True nếu thành công
        """
        json_string=json.dumps([item.__dict__ for item in arr_data],
                               default=str,indent=4,ensure_ascii=False)
        json_file=open(filename,'w',encoding='utf-8')
        json_file.write(json_string)
        json_file.close()

    def read_data(self, filename, ClassName, related_data=None):
        if not os.path.isfile(filename):
            return []

        with open(filename, 'r', encoding='utf-8') as file:
            arr_data = json.load(file)

        # Nếu có related_data (ví dụ: teachers_dict, students_dict), ánh xạ lại dữ liệu
        for obj in arr_data:
            for key, mapping in (related_data or {}).items():
                if key in obj and isinstance(obj[key], list):
                    obj[key] = [mapping[item_id] for item_id in obj[key] if item_id in mapping]

        return [ClassName(**obj) for obj in arr_data]