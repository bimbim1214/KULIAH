class persegipanjang:
    def __init__(self, panjang, lebar):
        self.panjang=panjang
        self.lebar=lebar
        
    def keliling(self):
        keliling = 2 * (self.panjang + self.lebar)
        return keliling
    
    def luas(self):
        luas = self.panjang * self.lebar
        return luas
    
    def __str__(self):
        return "persegi panjang" + "panjang  " + str(self.panjang) + " cm " + "lebar  " + str(self.lebar) + "keliling" + str(self.keliling()) + "luas" + str(self.luas())
    
panjang = int(input ("masukan panjang : " ))
lebar = int(input("masukan lebar : "))

persegi_panjang = persegipanjang(panjang , lebar)

print(persegi_panjang)
#print("keliling : ", persegi_panjang.keliling())
#print("luas : ", persegi_panjang.luas())