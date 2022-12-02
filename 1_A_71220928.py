print("====== Program Manipulasi String ======")
print('Pilihan Menu :')
print("1. Hitung Kata")
print("2. Ubah Kata")

dipileh = input("Pilihan anda :")
omongan = input("Masukkan sebuah kalimat/kata : ")

def hitungKata():
    hitung = omongan.replace(diubah,digenti)
    return hitung

def ubahKata():
    ubah = omongan.count(diitung)
    return ubah

if dipileh == "1":
    diitung = input("Masukan kata yang ingin dihitung : ")
    print("Terdapat sebanyak", ubahKata(), "kata", diitung, "di dalam kalimat")
elif dipileh == "2":
    diubah = input("Masukan kata yang ingin di ubah : ")
    digenti = input("masukkan kata pengganti : ")
    print("String berhasil diubah menjadi :", hitungKata())
else:
    print("Pilihan yang anda input tidak terdaftar di daftar pilihan")
