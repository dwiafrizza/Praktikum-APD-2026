import os
import pwinput
import data
from menu import menu_pengguna


def daftar_akun():
    os.system("cls")
    print("\n=== DAFTAR AKUN ===")
    username_baru = input("Masukkan username baru: ")
    password_baru = pwinput.pwinput("Masukkan password baru: ", mask="*")

    try:
        if username_baru == "" or password_baru == "":
            raise ValueError("Username dan password tidak boleh kosong.")
        elif username_baru in data.akun:
            raise ValueError("Username sudah digunakan. Silakan pakai username lain.")
    except ValueError as e:
        print(e)
    else:
        data.akun[username_baru] = {"password": password_baru, "role": "user"}
        print("Akun berhasil ditambahkan. Silakan login.")
    input("Tekan Enter untuk kembali...")


def login():
    os.system("cls")
    print("\n=== LOGIN ===")
    username = input("Username: ")
    password = pwinput.pwinput("Password: ", mask="*")

    try:
        if data.akun[username]["password"] != password:
            raise ValueError("Password salah.")
    except KeyError:
        print("Akun tidak ditemukan. Silakan daftar akun terlebih dahulu.")
        input("Tekan Enter untuk kembali...")
    except ValueError as e:
        print(e)
        input("Tekan Enter untuk kembali...")
    else:
        menu_pengguna(username, data.akun[username]["role"])