def assalamualaikum(nilai=1):       #membuat parameter nilai dengan defaultnya 1
    if nilai <= 0:          #jika mengisi nilai kurang dari atau sama dengan 0
        print("Nilai parameter jangan negatif atau 0")
        return
    else: 
        i = 0
        for i in range(nilai):          #membuat perulangan selama banyaknya nilai
            print("Assalamualaikum")

nilai = int(input("masukkan nilai :"))  #menambahkan banyaknya nilai
assalamualaikum(nilai) #menampilkan assalamualaikum sejumlah banyaknya nilai