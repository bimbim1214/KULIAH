class BungaMawar:
    def __init__(self, ukuran_bunga, warna):
        self.ukuran_bunga = ukuran_bunga
        self.warna = warna

    def buka_bunga(self):
        print("Bunga mawar terbuka dengan ukuran", self.ukuran_bunga, "cm dan warna", self.warna)

# Membuat objek bungaMawar
bunga_mawar_saya = BungaMawar(15, "Merah")

# Memanggil metode buka_bunga untuk objek bunga_mawar_saya
bunga_mawar_saya.buka_bunga()