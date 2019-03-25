class MhsTIF(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

c0 = MhsTIF('Bayu', 9, 'Sragen', 240000)
c1 = MhsTIF('Luluk', 10, 'Surakarta', 230000)
c2 = MhsTIF('Joko', 3, 'Ngawi', 250000)
c3 = MhsTIF('Saiful', 18, 'Klaten', 230000)
c4 = MhsTIF('Steven', 4, 'London', 240000)
c5 = MhsTIF('Jamilah', 32, 'Salatiga', 250000)
c6 = MhsTIF('Bambank', 13, 'Semarang', 245000)
c7 = MhsTIF('Suseno', 5, 'Wonogiri', 245000)
c8 = MhsTIF('Jarmo', 23, 'Klaten', 245000)
c9 = MhsTIF('Paiman', 64, 'Karanganyar', 270000)
c10 = MhsTIF('Khalid', 29, 'Purwodadi', 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

#No1
def cariKotaTinggal(list, target):
    a = []
    for i in list :
        if i.kotaTinggal == target:
            a.append(list.index(i))
    return a

a = cariKotaTinggal(Daftar, "London")
print(a)

#No2
def cariUangSakuTerkecil(list):
    temp = list[0].uangSaku
    for i in list[1:]:
        if i.uangSaku < temp:
            temp = i.uangSaku
    return temp

b = cariUangSakuTerkecil(Daftar)
print(b)

#No3
def cariUangSakuTerkecilObject(list):
    temp = [list[0]]
    for i in list[1:]:
        if i.uangSaku < temp[0].uangSaku:
            temp = [i]
        elif i.uangSaku == temp[0].uangSaku:
            temp.append(i)
    return temp

c = cariUangSakuTerkecilObject(Daftar)
print(c)

#No.4
def cariUangSakuKurang250k(list):
    temp = []
    for i in list:
        if i.uangSaku < 250000:
            temp.append(i)
    return temp

d = cariUangSakuKurang250k(Daftar)
for i in d:
    print(i.nama)


#No6

def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan)-1
    while low <= high:
        mid = (high+low)//2
        if kumpulan[mid] == target:
            return mid
        elif target < kumpulan[mid]:
            high = mid-1
        else:
            low = mid+1
    return False

kumpulan = [3, 4, 5, 9, 10, 13, 18, 23, 29, 32, 64]
print(binSe(kumpulan, 10))

#No7

def binSeMass(kumpulan, target):
    temp = []
    low = 0
    high = len(kumpulan)-1
    while low <= high :
        mid = (high+low)//2
        if kumpulan[mid] == target:
            midKiri = mid-1
            while kumpulan[midKiri] == target:
                temp.append(midKiri)
                midKiri = midKiri-1
            temp.append(mid)
            midKanan = mid+1
            while kumpulan[midKanan] == target:
                temp.append(midKanan)
                midKanan = midKanan+1
            return temp
        elif target < kumpulan[mid]:
            high = mid-1
        else:
            low = mid+1
    return False

kumpulan = [2, 4, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
print(binSeMass(kumpulan, 9))
