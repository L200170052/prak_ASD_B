class Pesan(object):
    """
        Sebuah class bernama Pesan.
        Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print("Kalimatku mempunyai" ,len(self.teks), "Karakter.")
    def perbarui(self,stringBaru):
        self.teks = stringBaru

    def apakahTerkandung(self, string):
        return string in self.teks

    def jmlkonso(self):
        vok = 0
        x = "aiueoAIUEO"
        for car in self.teks:
            if car not in x:
                vok += 1
        return(vok)
    
    def jmlvokal(self):
        vok = 0
        x = "aiueoAIUEO"
        for car in self.teks:
            if car in x:
                vok += 1
        return(vok)
    
