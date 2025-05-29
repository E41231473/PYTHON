print("Hello, World!")

if 5 > 6:
    print("Hello, World!")
else:
    print('5')
class variable:

    a = 10
    b = 20
    c = "benar"
    d = "salah"

    if a < b:
        print(c)
    else:
        print(d)

    if c == d:
        print("c sama dengan d")
    else:
        print("d sama dengan c")

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
        