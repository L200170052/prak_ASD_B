#No 2
class Mahasiswa(object):
    def __init__(self,nama,NIM,kota,us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM' + str(self.NIM) \
            +'. Tinggal di ' + self.kotaTinggal \
            +'. Uang saku Rp ' + str(self.uangSaku) \
            +' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self,s):
        print("Saya baru saja makan",s, "sambil belajar.")
        self.keadaan = 'kenyang'
#2a
    def ambilKotaTinggal(self):
        return self.kotaTinggal
#2b
    def perbaruikota(self, stringBaru):
        self.kotaTinggal = stringBaru
        print("kota sekarang",self.kotaTinggal)
#2c
    def tambahuangsaku (self, tambah):
        self.uangSaku += tambah
        print("uang saku sekarang",self.uangSaku)

print ("Silahkan tulis nama variabel lalu = Mahasiswa (.......) untuk menjalankan program")

    
    
