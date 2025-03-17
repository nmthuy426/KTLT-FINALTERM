from unidecode import unidecode

class User:
    def __init__(self, user_id: str, fullname: str, birthday: str, gender: str, password: str, role: str):
        self.user_id = user_id
        self.fullname = fullname
        self.birthday = birthday
        self.gender = gender
        self.email = self.generate_email(fullname, role)
        self.password = password

    @staticmethod
    def generate_email(fullname: str, role: str) -> str:
        fullname = unidecode(fullname)  # Loại bỏ dấu
        name_parts = fullname.split()
        first_name = name_parts[-1].lower()  # Lấy tên và viết thường
        initials = "".join(word[0].lower() for word in name_parts[:-1])  # Chữ cái đầu của họ và tên đệm

        if role == "student":
            return f"{first_name}{initials}@st.uel.edu.vn"
        elif role == "teacher":
            return f"{first_name}{initials}@uel.edu.vn"
        else:
            return None
