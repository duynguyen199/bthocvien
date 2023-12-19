# sinhVien=[{
#     "id":1,
#     "name":"A",
#     "diemToan":3,
#     "diemVan":4,
#     "diemHoa":5
# },
# {
#     "id":2,
#     "name":"B",
#     "diemToan":8,
#     "diemVan":8,
#     "diemHoa":4
# },
# {
#     "id":3,
#     "name":"C",
#     "diemToan":6,
#     "diemVan":5,
#     "diemHoa":3
# },
# {
#     "id":4,
#     "name":"D",
#     "diemToan":10,
#     "diemVan":10,
#     "diemHoa":5
# },
# {
#     "id":5,
#     "name":"E",
#     "diemToan":9,
#     "diemVan":9,
#     "diemHoa":9
# }]


# sinhVienCoDiemHoaDuoi5= [sv for sv in sinhVien if sv["diemHoa"]<5 ]
# print(sinhVienCoDiemHoaDuoi5)


# for sv in sinhVien:
#     diemTrungBinh= (sv["diemToan"] + sv["diemHoa"] + sv["diemVan"])//5
#     if diemTrungBinh <5:
#         print(sinhVien[diemTrungBinh])

class KhoaHoc:
    def __init__(self, maKhoaHoc,tenKhoaHoc,hinhThuc,hocPhi):
      self.maKhoaHoc=maKhoaHoc
      self.tenKhoaHoc=tenKhoaHoc
      self.hinhThuc=hinhThuc
      self.hocPhi=hocPhi
    def thongTinKhoaHoc(self):
        return """
            Thông tin khoá học:
            Mã Khoá Hoc: ${self.maKhoaHoc}
            Tên Khoá Hoc:${self.tenKhoaHoc}
            Hình thức:${self.hinhThuc}
            Học Phí:${self.hocPhi}
        
        """

class HocVien(KhoaHoc):
    def __init__(self,maHV,tenHV,ngaySinh,khoaHoc, maKhoaHoc,tenKhoaHoc,hinhThuc,hocPhi):
        super().__init__( maKhoaHoc,tenKhoaHoc,hinhThuc,hocPhi)
        self.maHV=maHV
        self.tenHV=tenHV
        self.ngaySinh=ngaySinh
        self.khoaHoc = khoaHoc
    def dangKiKhoaHoc(self,khoaHoc):
        khoaHoc = self.maKhoaHoc
        khoaHoc=self.tenKhoaHoc
        khoaHoc=self.hinhThuc
        khoaHoc=self.hocPhi
        return khoaHoc
    def hienThiKhoaHoc():
        
        return KhoaHoc.thongTinKhoaHoc()
        