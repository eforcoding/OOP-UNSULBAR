#class utama
class BangunDatar:
    def __init__(self):
        self.sisi = 0
    
    def luas(self):
        pass
    def volume(self):
        pass
#class turunan
class Persegi(BangunDatar):
    def __init__(self):
        BangunDatar.__init__(self)
    
    def luas(self):
        return self.sisi ** 2
    def volume(self):
        return self.sisi**3

class PersegiSegitiga(BangunDatar):
    def __init__(self):
        BangunDatar.__init__(self)
        self.tinggi = 0
    
    def luas(self):
        return 0.5 * self.sisi * self.tinggi
    def volume(self):
        return self.alas * self.tinggi * self.sisi / 3

class Lingkaran(BangunDatar):
    def __init__(self):
        BangunDatar.__init__(self)
    
    def luas(self):
        return 3.14 * (self.sisi/2) ** 2
    def volume(self):
        return (4/3) * 3.14 * (self.jarijari**3)

# Contoh penggunaan
print("Nama : EFORTUNTRIO")
print("NIM : D0221375")
print("-----LUAS PERSEGI-----")
persegi = Persegi()
persegi.sisi = int(input("1. Masukkan sisi persegi: "))
print(f"jadi, Luas persegi adalah : {persegi.luas()}")
print("-----VOLUME PERSEGI-----")
persegi.sisi = int(input("2. masukkan sisi persegi: "))
print(f"jadi, volume persegi adalah : {persegi.volume()}")
print("-----LUAS SEGITIGA-----")
persegi_segitiga = PersegiSegitiga()
persegi_segitiga.sisi = int(input("1. Masukkan sisi persegi segitiga: "))
persegi_segitiga.tinggi = int(input("2. Masukkan tinggi persegi segitiga: "))
print(f"jadi, Luas persegi segitiga adalah : {persegi_segitiga.luas()}")
print("-----VOLUME SEGITIGA-----")
persegi_segitiga.alas = int(input("1. Masukkan alas persegi segitiga: "))
persegi_segitiga.tinggi = int(input("2. Masukkan tinggi persegi segitiga: "))
persegi_segitiga.sisi = int(input("3. Masukkan sisi persegi segitiga: "))
print(f"jadi, volume persegi segitiga adalah : {persegi_segitiga.volume()}")
print("-----LUAS LINGKARAN-----")
lingkaran = Lingkaran()
lingkaran.sisi = int(input("1. Masukkan jari-jari lingkaran: "))
print(f"jadi, Luas lingkaran adalah : {lingkaran.luas()}")
print("-----VOLUME LINGKARANG-----")
lingkaran.jarijari = int(input("1. Masukkan jari-jari lingkaran: "))
print(f"jadi, volume lingkaran adalah : {lingkaran.volume()}")


