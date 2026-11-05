import os
from prettytable import PrettyTable
import data
from validasi import cek_waktu, cari_jenis
from tampilan import input_nomor, tampilkan_jenis


def hitung_helm(daftar_nomor, indeks, status):
    if indeks == len(daftar_nomor):
        return 0
    if data.helm[daftar_nomor[indeks]]["status"] == status:
        return 1 + hitung_helm(daftar_nomor, indeks + 1, status)
    return hitung_helm(daftar_nomor, indeks + 1, status)


def titip_helm(username):
    os.system("cls")
    print("\n=== TITIP HELM ===")
    nama_pemilik = input("Masukkan nama pemilik helm: ")
    print("Pilih jenis helm:")
    tampilkan_jenis()
    pilih_jenis = input("Masukkan nomor jenis helm: ")
    waktu = input("Masukkan waktu penitipan (contoh 08.30): ")
    jenis_dipilih = cari_jenis(pilih_jenis)

    try:
        if nama_pemilik == "" or waktu == "":
            raise ValueError("Nama pemilik dan waktu penitipan tidak boleh kosong.")
        elif jenis_dipilih == "":
            raise ValueError("Nomor jenis helm tidak tersedia.")
        elif cek_waktu(waktu) == False:
            raise ValueError("Format waktu tidak valid. Gunakan format 08.30.")
    except ValueError as e:
        print(e)
    else:
        data.helm[str(data.nomor_berikutnya)] = {
            "pemilik": nama_pemilik,
            "jenis": jenis_dipilih,
            "waktu": waktu,
            "status": "Dititipkan",
            "akun": username
        }
        print("Data helm berhasil ditambahkan. Nomor penitipan:", data.nomor_berikutnya)
        data.nomor_berikutnya += 1
    finally:
        input("Tekan Enter untuk kembali...")


def lihat_data(role, username):
    os.system("cls")
    print("\n=== DATA HELM ===")
    tabel = PrettyTable()
    tabel.field_names = ["Nomor", "Pemilik", "Jenis", "Waktu", "Status"]
    tabel.align["Pemilik"] = "l"
    ada_data = False

    for nomor, item in data.helm.items():
        if role == "admin" or item["akun"] == username:
            tabel.add_row([nomor, item["pemilik"], item["jenis"],
                           item["waktu"], item["status"]])
            ada_data = True

    if ada_data == False:
        print("Belum ada data helm.")
    else:
        print(tabel)
        if role == "admin":
            daftar_nomor = list(data.helm.keys())
            ringkasan = PrettyTable()
            ringkasan.field_names = ["Status", "Total"]
            ringkasan.add_row(["Dititipkan", hitung_helm(daftar_nomor, 0, "Dititipkan")])
            ringkasan.add_row(["Sudah Diambil", hitung_helm(daftar_nomor, 0, "Sudah Diambil")])
            print("\nRingkasan:")
            print(ringkasan)
    input("Tekan Enter untuk kembali...")


def ubah_data(role, username):
    os.system("cls")
    print("\n=== UBAH DATA HELM ===")
    nomor_cari = input_nomor()

    try:
        data_ketemu = data.helm[nomor_cari]
        if role != "admin" and data_ketemu["akun"] != username:
            raise ValueError("Data helm tidak ditemukan.")
        elif data_ketemu["status"] == "Sudah Diambil":
            raise ValueError("Data helm yang sudah diambil tidak dapat diubah.")

        print("Nama pemilik saat ini:", data_ketemu["pemilik"])
        print("Jenis helm saat ini  :", data_ketemu["jenis"])
        nama_baru = input("Masukkan nama pemilik baru (kosongkan jika tetap): ")
        print("Pilih jenis helm baru:")
        tampilkan_jenis()
        jenis_baru = input("Masukkan nomor jenis baru (kosongkan jika tetap): ")
        jenis_dipilih = cari_jenis(jenis_baru)

        if jenis_baru != "" and jenis_dipilih == "":
            raise ValueError("Nomor jenis helm tidak tersedia.")
    except KeyError:
        print("Data helm tidak ditemukan.")
    except ValueError as e:
        print(e)
    else:
        if nama_baru != "":
            data_ketemu["pemilik"] = nama_baru
        if jenis_dipilih != "":
            data_ketemu["jenis"] = jenis_dipilih
        print("Data helm berhasil diubah.")
    input("Tekan Enter untuk kembali...")


def ubah_status():
    os.system("cls")
    print("\n=== UBAH STATUS PENGAMBILAN ===")
    nomor_cari = input_nomor()

    try:
        print("Status sekarang:", data.helm[nomor_cari]["status"])
        print("1. Dititipkan")
        print("2. Sudah diambil")
        pilih_status = input("Masukkan status baru: ")

        if pilih_status == "1":
            data.helm[nomor_cari]["status"] = "Dititipkan"
        elif pilih_status == "2":
            data.helm[nomor_cari]["status"] = "Sudah Diambil"
        else:
            raise ValueError("Pilihan status tidak valid.")
    except KeyError:
        print("Nomor penitipan tidak ditemukan.")
    except ValueError as e:
        print(e)
    else:
        print("Status berhasil diubah.")
    input("Tekan Enter untuk kembali...")


def hapus_data():
    os.system("cls")
    print("\n=== HAPUS DATA HELM ===")
    nomor_cari = input_nomor()

    try:
        konfirmasi = input(
            "Hapus data helm milik " + data.helm[nomor_cari]["pemilik"] + "? (y/n): "
        )

        if konfirmasi == "y" or konfirmasi == "Y":
            del data.helm[nomor_cari]
            print("Data helm berhasil dihapus.")
        elif konfirmasi == "n" or konfirmasi == "N":
            print("Data helm tidak jadi dihapus.")
        else:
            print("Jawab y atau n. Data helm tidak jadi dihapus.")
    except KeyError:
        print("Nomor penitipan tidak ditemukan.")
    input("Tekan Enter untuk kembali...")
    