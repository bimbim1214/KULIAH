def konversi_suhu(C, F):
    fahreinhet = (9/5 * C) + 32
    celcius = 5/9 * (F + 32)
    print("nilai satuan suhu celcius: ", celcius)
    print("nilai satuan suhu fahrenheit: ", fahreinhet)

celcius = float(input("masukan nilai celcius: "))
fahreinhet = float(input("masukan nilai fahreinhet: "))

konversi_suhu(celcius, fahreinhet)