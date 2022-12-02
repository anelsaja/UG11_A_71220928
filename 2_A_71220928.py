omongan = input("Masukkan kata :")
piranghuruf = int(len(omongan))

def cetakHuruf(omongan):
    if piranghuruf % 2 == 0:
        pisan = omongan[0:3]
        karinan = omongan[-3:]
        print("Huruf yang diambil pada kata", omongan, "adalah", pisan, "dan" , karinan)
    else:
        ngger = int((piranghuruf-3)/2)
        teluhuruf = omongan[ngger:-ngger]
        print("Huruf yang diambil pada kata", omongan, "adalah", teluhuruf)
        return
    
cetakHuruf(omongan)
        



