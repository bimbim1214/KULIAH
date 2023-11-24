import tkinter as tk
from tkinter import messagebox

import sqlite3

def simpan_data_ke_sqlite(nilai1,nilai2, prodi_terpilih):
# Membuka atau membuat database SQLite
    conn = sqlite3.connect(kelasB.db)
    cursor = conn.cursor()
# Membuat tabel jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS hasil_prediksi
    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nilai1 INTEGER, 
    nilai2 INTEGER,
    prodi_terpilih TEXT)''')
# Memasukkan data mata pelajaran ke dalam tabel
    cursor.execute("INSERT INTO hasil_prediksi (mata_pelajaran, nilai, prodi_terpilih) VALUES ()",
    (nilai1, nilai2, prodi_terpilih))
# Melakukan commit dan menutup koneksi
    conn.commit()
    conn.close()


top = tk.Tk()
top.title("Pemrograman Kelas B")
top.geometry("400x400")
top.resizable(False, False)

inputframe = tk.LabelFrame(top)
inputframe.pack(padx= 10, pady= 10, fill = "x", expand= True)



#bikin label untuk judul
var = tk.Label(inputframe, text = "Aplikasi Prediksi Prodi Pilihan")
var.pack()
#bikin inputan
input= tk.Label(inputframe, text = "Masukan Nama Depan: ")
input.pack(padx = 10, pady = 5, fill = "x", expand=True)

E1= tk.Entry(inputframe)
E1.pack(padx = 10, pady = 5, fill = "x", expand=True)

#bikin input 2
input= tk.Label(inputframe, text = "Masukan Nama Belakang: ")
input.pack(padx = 10, pady = 5, fill = "x", expand=True)

E2= tk.Entry(inputframe)
E2.pack(padx = 10, pady = 5, fill = "x", expand=True)

#bikin button
def onClickbut():
    Nama_Depan = E1.get()
    Nama_Belakang = E2.get()
    print("nama kamu adalah: " + Nama_Depan + " " + Nama_Belakang)
    messagebox.showinfo("info", "nama kamu adalah: " + Nama_Depan + " " + Nama_Belakang)
tombol = tk.Button(inputframe, text= "submit", command=onClickbut)
tombol.pack(padx = 10, pady = 5, fill = "x", expand=True)

top.mainloop()