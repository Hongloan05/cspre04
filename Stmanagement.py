import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# Quản lý học viên và đăng ký khóa học

class Hocvien:
    # Khởi tạo phương thức
    def __init__(self, maHV, tenHV, ngaySinh, khoaHoc=None):
        self.maHV = maHV
        self.tenHV = tenHV
        self.ngaySinh = ngaySinh
        self.khoaHoc = khoaHoc if khoaHoc is not None else []  # Khởi tạo danh sách khóa học

    # Phương thức đăng ký khóa học
    def dangKyKhoaHoc(self, khoaHoc):
        self.khoaHoc.append(khoaHoc)
        print(f"Học viên {self.tenHV} đã đăng ký khóa học {khoaHoc.tenKhoaHoc}.")

    # Phương thức hiển thị các khóa học đã đăng ký
    def hienThiKhoaHoc(self):
        if self.khoaHoc:
            print(f"Học viên {self.tenHV} đã đăng ký các khóa học:")
            for khoa in self.khoaHoc:
                print(f" - {khoa.tenKhoaHoc}")
        else:
            print(f"Học viên {self.tenHV} chưa đăng ký khóa học nào.")

# Định nghĩa lớp Khóa Học
class KhoaHoc:
    def __init__(self, maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi):
        self.maKhoaHoc = maKhoaHoc
        self.tenKhoaHoc = tenKhoaHoc
        self.hinhThuc = hinhThuc
        self.hocPhi = hocPhi

    # Phương thức hiển thị thông tin khóa học
    def thongTinKhoaHoc(self):
        print(f"Khóa học: {self.tenKhoaHoc}")
        print(f" - Mã khóa học: {self.maKhoaHoc}")
        print(f" - Hình thức: {self.hinhThuc}")
        print(f" - Học phí: {self.hocPhi} VND")


# Tạo các đối tượng mẫu
# Khóa học
khoaHoc1 = KhoaHoc("KH01", "Lập trình Python", "Online", 1500000)
khoaHoc2 = KhoaHoc("KH02", "Lập trình Java", "Offline", 2000000)

# Học viên
hocVien1 = Hocvien("HV01", "Nguyễn Văn A", "01/01/2000")
hocVien2 = Hocvien("HV02", "Trần Thị B", "05/05/1998")

# Thực hiện một số thao tác
# Học viên 1 đăng ký khóa học
hocVien1.dangKyKhoaHoc(khoaHoc1)
hocVien1.dangKyKhoaHoc(khoaHoc2)

# Học viên 2 đăng ký khóa học
hocVien2.dangKyKhoaHoc(khoaHoc1)

# Hiển thị danh sách khóa học của từng học viên
hocVien1.hienThiKhoaHoc()
hocVien2.hienThiKhoaHoc()

# Hiển thị thông tin chi tiết về khóa học
khoaHoc1.thongTinKhoaHoc()
khoaHoc2.thongTinKhoaHoc()
