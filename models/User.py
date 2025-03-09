class User:
    def __init__(self, user_id: str, fullname: str, birthday: str, gender: str, email: str, password: str):
        self.user_id = user_id
        self.fullname = fullname
        self.birthday = birthday
        self.gender = gender
        self.email = email
        self.password = password