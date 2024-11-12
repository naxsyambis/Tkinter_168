import tkinter as tk  # Mengimport library tkinter dan memberinya alias 'tk'
from tkinter import messagebox  # Mengimport messagebox untuk menampilkan pesan peringatan

# Fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    try:
        # Loop untuk memvalidasi setiap nilai pada entri
        for entry in entries:
            nilai = int(entry.get())  # Mengonversi nilai input ke integer
            # Memeriksa apakah nilai antara 0 dan 100
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
        # Jika semua nilai valid, tampilkan hasil prediksi
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi", fg="black")  # Warna teks hasil prediksi
    except ValueError:
        # Tampilkan pesan kesalahan jika ada nilai yang tidak valid
        messagebox.showerror("Kesalahan Input", "Pastikan semua input adalah angka antara 0 dan 100.")

# Pengaturan jendela utama Tkinter
root = tk.Tk()  # Membuat instance Tk untuk jendela utama
root.title("Aplikasi Prediksi Prodi Pilihan")  # Mengatur judul jendela
root.geometry("500x600")  # Mengatur ukuran jendela
root.configure(bg="#d9f2e6")  # Mengatur warna latar belakang jendela

# Label Judul
judul_label = tk.Label(
    root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16), bg="#d9f2e6", fg="blue")  # Membuat label judul dengan font, warna latar, dan warna teks khusus
judul_label.pack(pady=20)  # Menambahkan padding vertikal

# Frame untuk memasukkan nilai
frame_input = tk.Frame(root, bg="#d9f2e6")  # Membuat frame untuk input dengan warna latar khusus
frame_input.pack(pady=10)  # Menambahkan padding vertikal

# Membuat entri untuk nilai mata pelajaran
entries = []  # List untuk menyimpan entry widget
for i in range(10):  # Loop untuk membuat 10 entri
    tk.Label(
        frame_input, text=f"Nilai Mata Pelajaran {i+1}:", font=("Arial", 12), bg="#d9f2e6", fg="black").grid(row=i, column=0, padx=10, pady=5)  # Label untuk setiap entri, dengan teks dan warna khusus
    entry = tk.Entry(
        frame_input, width=10, font=("Arial", 12), bg="#ffffff", fg="black")  # Membuat entry untuk nilai dengan ukuran dan warna khusus
    entry.grid(row=i, column=1, padx=10, pady=5)  # Menempatkan entry di kolom kedua pada setiap baris
    entries.append(entry)  # Menyimpan entry dalam list entries

# Tombol untuk prediksi
prediksi_button = tk.Button(
    root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12), bg="#007acc", fg="white")  # Membuat tombol untuk memicu fungsi hasil_prediksi
prediksi_button.pack(pady=30)  # Menambahkan padding vertikal untuk tombol

# Label untuk menampilkan hasil
hasil_label = tk.Label(
    root, text="", font=("Arial", 14, "italic", "bold"), fg="green", bg="#d9f2e6")  # Label kosong untuk menampilkan hasil prediksi dengan warna teks dan latar khusus
hasil_label.pack(pady=20)  # Menambahkan padding vertikal untuk label hasil

# Menjalankan loop utama
root.mainloop()  # Memulai aplikasi dan menampilkan jendela utama
