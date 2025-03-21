import json
import os


class Grade:
    def __init__(self, student_id, class_id, formative1=0, formative2=0, midterm=0, finalterm=0, average=float):
        self.student_id = student_id
        self.class_id = class_id
        self.formative1 = float(formative1) if formative1 is not None else 0.0
        self.formative2 = float(formative2) if formative2 is not None else 0.0
        self.midterm = float(midterm) if midterm is not None else 0.0
        self.finalterm = float(finalterm) if finalterm is not None else 0.0
        self.average = self.calculate_average()

    def calculate_average(self):
        """Tính điểm trung bình có trọng số."""
        return round((self.formative1 + self.formative2 + self.midterm * 2 + self.finalterm * 3) / 7, 2)


    @staticmethod
    def save_to_file(grades, filename="grades.json"):
        """Lưu danh sách điểm vào file JSON."""
        data = []
        if os.path.exists(filename):
            try:
                with open(filename, "r", encoding="utf-8") as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []  # Nếu file bị lỗi, bắt đầu từ danh sách rỗng

        # Hợp nhất dữ liệu cũ và mới (tránh mất dữ liệu)
        existing_students = {g["student_id"]: g for g in data}
        for grade in grades:
            existing_students[grade.student_id] = grade.to_dict()

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(list(existing_students.values()), file, indent=4)

    @staticmethod
    def load_from_file(filename="grades.json"):
        """Đọc danh sách điểm từ file JSON."""
        if not os.path.exists(filename):
            return []

        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Grade(**item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def __str__(self):
        return (f"SV: {self.student_id} | Lớp: {self.class_id} | "
                f"Điểm: {self.formative1}, {self.formative2}, {self.midterm}, {self.finalterm} | "
                f"TB: {self.average}")