def sapa(nama="Abdullah"):
    if len(nama) < 3:
        print("nama terlalu pendek")
        return
    print("halo, " + nama + "!")
    
nama_pengguna = input("masukan nama anda: ")
sapa(nama_pengguna)
sapa()
