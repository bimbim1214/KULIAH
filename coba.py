import tkinter as tk
import sqlite3

# Fungsi untuk menentukan prediksi fakultas
def prediksi_fakultas(biologi, fisika, inggris):
    if biologi > fisika and biologi > inggris:
        return "Kedokteran"
    elif fisika > biologi and fisika > inggris:
        return "Teknik"
    elif inggris > biologi and inggris > fisika:
        return "Bahasa"
    else:
        return "Tidak dapat memprediksi"

# Fungsi untuk menyimpan data ke SQLite
def simpan_data(nama, biologi, fisika, inggris):
    prediksi = prediksi_fakultas(biologi, fisika, inggris)
    
    # Menyimpan data ke database SQLite
    connection = sqlite3.connect("data_siswa.db")
    cursor = connection.cursor()
    
    # Membuat tabel jika belum ada
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT,
            biologi INTEGER,
            fisika INTEGER,
            inggris INTEGER,
            prediksi_fakultas TEXT
        )
    ''')

    # Menambahkan entry ke tabel
    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama, biologi, fisika, inggris, prediksi))
    
    # Commit perubahan dan menutup koneksi
    connection.commit()
    connection.close()

# Fungsi yang akan dijalankan saat tombol submit ditekan
def submit_nilai():
    # Mengambil nilai dari inputan pengguna
    nama = entry_nama.get()
    nilai_biologi = int(entry_biologi.get())
    nilai_fisika = int(entry_fisika.get())
    nilai_inggris = int(entry_inggris.get())

    # Menyimpan data ke SQLite
    simpan_data(nama, nilai_biologi, nilai_fisika, nilai_inggris)

# Membuat GUI menggunakan Tkinter
root = tk.Tk()
root.title("Input Nilai Siswa")

# Label dan Entry untuk Nama Siswa
label_nama = tk.Label(root, text="Nama Siswa:")
label_nama.pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

# Label dan Entry untuk Nilai Biologi
label_biologi = tk.Label(root, text="Nilai Biologi:")
label_biologi.pack()
entry_biologi = tk.Entry(root)
entry_biologi.pack()

# Label dan Entry untuk Nilai Fisika
label_fisika = tk.Label(root, text="Nilai Fisika:")
label_fisika.pack()
entry_fisika = tk.Entry(root)
entry_fisika.pack()

# Label dan Entry untuk Nilai Inggris
label_inggris = tk.Label(root, text="Nilai Inggris:")
label_inggris.pack()
entry_inggris = tk.Entry(root)
entry_inggris.pack()

# Tombol Submit
button_submit = tk.Button(root, text="Submit", command=submit_nilai)
button_submit.pack()

# Menjalankan aplikasi Tkinter
root.mainloop()
