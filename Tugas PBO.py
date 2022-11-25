from abc import ABC, abstractmethod


from math import pi

class BangunDatar(ABC):
    @abstractmethod
    def luas(self):
        pass

class Lingkaran(BangunDatar):
    def _init_(self, jari = 0):
        self.jari = jari

    def luas(self):
        return pi * (self.jari**2)

class Persegi(BangunDatar):
    def _init_(self, sisi = 0):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

class Segitiga(BangunDatar):
    def _init_(self, alas = 0, tinggi = 0):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi
    
    
lingkaran = Lingkaran()
segitiga = Segitiga()
persegi = Persegi()
luas = 0

while True:
    print()
    print("""
a. Menghitung Luas Segitiga
b. Menghitung Luas Persegi
c. Menghitung Luas Lingkaran
d. Stop""")
    pilihan = input("=> ")

    if pilihan == 'a':
        segitiga.alas = float(input("Input Alas: "))
        segitiga.tinggi = float(input("Input Tinggi: "))
        luas = segitiga.luas()
    elif pilihan == 'b':
        persegi.sisi = float(input("Input Sisi: "))
        luas = persegi.luas()
    elif pilihan == 'c':
        lingkaran.jari = float(input("Input Jari-jari: "))
        luas = lingkaran.luas()
    elif pilihan == 'd':
        break
    else:
        print("Inputan Salah!")
    
    print("Luasnya Yaitu: ", luas)

print("Terima Kasih")
