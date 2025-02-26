class SinhVien(NguoiDung):
    def __init__(self, ma_so, ho_ten):
        super().__init__(ma_so, ho_ten)
        self.diem_so = {}  # Lưu điểm theo dạng {ma_mon: diem}

    def them_diem(self, ma_mon, diem):
        self.diem_so[ma_mon] = diem

    def tinh_diem_trung_binh(self, danh_sach_mon_hoc):
        tong_diem = 0
        tong_tin_chi = 0
        for ma_mon, diem in self.diem_so.items():
            mon_hoc = danh_sach_mon_hoc.get(ma_mon)
            if mon_hoc:
                tong_diem += diem * mon_hoc.so_tin_chi
                tong_tin_chi += mon_hoc.so_tin_chi
        return round(tong_diem / tong_tin_chi, 2) if tong_tin_chi > 0 else 0
