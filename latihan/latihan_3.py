def persegiPanjang(panjang, tinggi):        #membuat fungsi dengan parameter panjang dan tinggi
    if panjang <= 0 or tinggi <= 0:         #jika nilai kedua parameter kurang dari atau sama dengan 0
        print("Nilai parameter jangan 0 atau negatif")
        return
    else:                                   #jika nilai kedua parameter lebih dari 0
        luas = panjang * tinggi             #membuat variable luas yang berisikan panjang kali tinggi
        print("Luas persegi panjang: ",luas)


panjang = int(input("Masukkan panjang (cm): "))
tinggi = int(input("Masukkan tinggi (cm): "))
persegiPanjang(panjang, tinggi)