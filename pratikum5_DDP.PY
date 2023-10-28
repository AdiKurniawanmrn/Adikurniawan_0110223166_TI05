#no1
list=["vario110", "motor", "110", "putih"," tubles"]

print(list)

list.append("7juta",)
list.append("roda 2")
list.insert(2,"Honda")

print(list)
#no 2
import math

def hitung_luas(bentuk, *args):
    match bentuk:
        case "persegi":
            sisi = args[0]
            luas_persegi = sisi ** 2
            return luas_persegi
        case "lingkaran":
            jari_jari = args[0]
            luas_lingkaran = math.pi * jari_jari ** 2
            return luas_lingkaran
        case "segitiga":
            alas, tinggi = args[0], args[1]
            luas_segitiga = 0.5 * alas * tinggi
            return luas_segitiga
       

print("Luas Persegi:", hitung_luas("persegi", 12))
print("Luas Lingkaran:", hitung_luas("lingkaran", 8))
print("Luas Segitiga:", hitung_luas("segitiga",7,5))
