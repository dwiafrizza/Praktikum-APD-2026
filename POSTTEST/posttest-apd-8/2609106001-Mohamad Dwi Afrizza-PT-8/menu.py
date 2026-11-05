import os
from penitipan import titip_helm, lihat_data, ubah_data, ubah_status, hapus_data


def menu_pengguna(username, role):
    while True:
        os.system("cls")
        print("\n=== MENU PENITIPAN HELM ===")
        print("Login sebagai:", username, "(" + role + ")")
        print("1. Titip helm")
        print("2. Lihat data helm")
        print("3. Ubah data helm")

        if role == "admin":
            print("4. Ubah status pengambilan")
            print("5. Hapus data helm")
            print("6. Logout")
            kode_logout = "6"
        else:
            print("4. Logout")
            kode_logout = "4"

        pilihan = input("Masukkan menu yang dipilih: ")

        if pilihan == "1":
            titip_helm(username)
        elif pilihan == "2":
            lihat_data(role, username)
        elif pilihan == "3":
            ubah_data(role, username)
        elif pilihan == "4" and role == "admin":
            ubah_status()
        elif pilihan == "5" and role == "admin":
            hapus_data()
        elif pilihan == kode_logout:
            print("Logout berhasil.")
            break
        else:
            print("Menu tidak valid.")
            input("Tekan Enter untuk kembali...")