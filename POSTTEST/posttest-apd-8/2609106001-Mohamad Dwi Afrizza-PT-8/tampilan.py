import os
from prettytable import PrettyTable
import data


def menu_awal():
    os.system("cls")
    tabel = PrettyTable()
    tabel.field_names = ["No", "Menu"]
    tabel.align["Menu"] = "l"
    tabel.add_row(["1", "Login"])
    tabel.add_row(["2", "Daftar akun"])
    tabel.add_row(["3", "Keluar"])
    print("\n=== SISTEM TITIP HELM ===")
    print(tabel)
    pilihan_awal = input("Masukkan menu yang dipilih: ")
    return pilihan_awal


def input_nomor():
    nomor_cari = input("Masukkan nomor penitipan: ")
    return nomor_cari


def tampilkan_jenis():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Jenis Helm"]
    tabel.align["Jenis Helm"] = "l"
    no = 1
    for jenis in data.daftar_jenis:
        tabel.add_row([no, jenis])
        no += 1
    print(tabel)