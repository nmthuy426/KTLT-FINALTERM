class Teacher(User):
    def __init__(self,Fullname, Username, Password):
        super().__init__(Fullname, Username, Password)

    def nhap_diem(self, sinh_vien, ma_mon, diem):
        sinh_vien.them_diem(ma_mon, diem)