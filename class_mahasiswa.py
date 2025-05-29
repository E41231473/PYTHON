class mahasiswa:
    def __init__(self,nama,umur,nilai):
        self.nama = nama
        self.umur = umur
        self.nilai = nilai

    def cek_nilai(self):
        if self.nilai < 80:
            print("remidi")
        else:
            print("lulus")

m1 = mahasiswa("willy",21,79)
m1.cek_nilai()

class mahasiswa2:
    def __init__(self, nama, umur, nilai):
        self.nama = nama
        self.umur = umur
        self.nilai = nilai

    def cek_nilai(self):
        if self.nilai < 80:
            hasil = "remidi"
        else:
            hasil = "lulus"
        print(self.nama + " = " + hasil)


m1 = mahasiswa2("diana", 19, 80)
m1.cek_nilai()

class mahasiswa3:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai
    
    def cek_nilai(self):
        if self.nilai >= 80:
            print("lolos")
        else:
            print("gagal")
        print(self.nama + "=" + str(self.nilai))

m2 = mahasiswa3("rudi", 20)
m2.cek_nilai()