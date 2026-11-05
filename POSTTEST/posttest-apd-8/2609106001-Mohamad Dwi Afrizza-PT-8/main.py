from tampilan import menu_awal
from autentikasi import login, daftar_akun

while True:
    pilihan_awal = menu_awal()

    if pilihan_awal == "1":
        login()
    elif pilihan_awal == "2":
        daftar_akun()
    elif pilihan_awal == "3":
        print("Program selesai. Terima kasih sudah menggunakan Sistem Titip Helm.")
        break
    else:
        print("Menu tidak valid.")
        input("Tekan Enter untuk kembali...")