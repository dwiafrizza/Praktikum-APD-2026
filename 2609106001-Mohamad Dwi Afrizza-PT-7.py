import os

akun = {"admin": {"password": "admin123", "role": "admin"}}
helm = {}
nomor_berikutnya = 1
daftar_jenis = ("Full Face", "Half Face", "Open Face", "Modular")
angka = "0123456789"


def cek_waktu(waktu):
    waktu_valid = False
    if len(waktu) == 5 and waktu[2] == ".":
        if (waktu[0] in angka and waktu[1] in angka
                and waktu[3] in angka and waktu[4] in angka):
            if waktu[0:2] < "24" and waktu[3:5] < "60":
                waktu_valid = True
    return waktu_valid


def cari_jenis(pilih_jenis):
    jenis_dipilih = ""
    no = 1
    for jenis in daftar_jenis:
        if pilih_jenis == str(no):
            jenis_dipilih = jenis
        no += 1
    return jenis_dipilih


def menu_awal():
    os.system("cls")
    print("\n=== SISTEM TITIP HELM ===")
    print("1. Login")
    print("2. Daftar akun")
    print("3. Keluar")
    pilihan_awal = input("Masukkan menu yang dipilih: ")
    return pilihan_awal


def input_nomor():
    nomor_cari = input("Masukkan nomor penitipan: ")
    return nomor_cari


def hitung_helm(daftar_nomor, indeks, status):
    if indeks == len(daftar_nomor):
        return 0
    if helm[daftar_nomor[indeks]]["status"] == status:
        return 1 + hitung_helm(daftar_nomor, indeks + 1, status)
    return hitung_helm(daftar_nomor, indeks + 1, status)


def tampilkan_jenis():
    no = 1
    for jenis in daftar_jenis:
        print(str(no) + ". " + jenis)
        no += 1


def daftar_akun():
    os.system("cls")
    print("\n=== DAFTAR AKUN ===")
    username_baru = input("Masukkan username baru: ")
    password_baru = input("Masukkan password baru: ")

    try:
        if username_baru == "" or password_baru == "":
            raise ValueError("Username dan password tidak boleh kosong.")
        elif username_baru in akun:
            raise ValueError("Username sudah digunakan. Silakan pakai username lain.")
    except ValueError as e:
        print(e)
    else:
        akun[username_baru] = {"password": password_baru, "role": "user"}
        print("Akun berhasil ditambahkan. Silakan login.")
    input("Tekan Enter untuk kembali...")


def login():
    os.system("cls")
    print("\n=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")

    try:
        if akun[username]["password"] != password:
            raise ValueError("Password salah.")
    except KeyError:
        print("Akun tidak ditemukan. Silakan daftar akun terlebih dahulu.")
        input("Tekan Enter untuk kembali...")
    except ValueError as e:
        print(e)
        input("Tekan Enter untuk kembali...")
    else:
        menu_pengguna(username, akun[username]["role"])


def titip_helm(username):
    global nomor_berikutnya
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
        helm[str(nomor_berikutnya)] = {
            "pemilik": nama_pemilik,
            "jenis": jenis_dipilih,
            "waktu": waktu,
            "status": "Dititipkan",
            "akun": username
        }
        print("Data helm berhasil ditambahkan. Nomor penitipan:", nomor_berikutnya)
        nomor_berikutnya += 1
    finally:
        input("Tekan Enter untuk kembali...")


def lihat_data(role, username):
    os.system("cls")
    print("\n=== DATA HELM ===")
    ada_data = False

    for nomor, data in helm.items():
        if role == "admin" or data["akun"] == username:
            print("\nNomor   :", nomor)
            print("Pemilik :", data["pemilik"])
            print("Jenis   :", data["jenis"])
            print("Waktu   :", data["waktu"])
            print("Status  :", data["status"])
            ada_data = True

    if ada_data == False:
        print("Belum ada data helm.")
    elif role == "admin":
        daftar_nomor = list(helm.keys())
        print("\nTotal dititipkan    :", hitung_helm(daftar_nomor, 0, "Dititipkan"))
        print("Total sudah diambil :", hitung_helm(daftar_nomor, 0, "Sudah Diambil"))
    input("Tekan Enter untuk kembali...")


def ubah_data(role, username):
    os.system("cls")
    print("\n=== UBAH DATA HELM ===")
    nomor_cari = input_nomor()

    try:
        data_ketemu = helm[nomor_cari]
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
        print("Status sekarang:", helm[nomor_cari]["status"])
        print("1. Dititipkan")
        print("2. Sudah diambil")
        pilih_status = input("Masukkan status baru: ")

        if pilih_status == "1":
            helm[nomor_cari]["status"] = "Dititipkan"
        elif pilih_status == "2":
            helm[nomor_cari]["status"] = "Sudah Diambil"
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
            "Hapus data helm milik " + helm[nomor_cari]["pemilik"] + "? (y/n): "
        )

        if konfirmasi == "y" or konfirmasi == "Y":
            del helm[nomor_cari]
            print("Data helm berhasil dihapus.")
        elif konfirmasi == "n" or konfirmasi == "N":
            print("Data helm tidak jadi dihapus.")
        else:
            print("Jawab y atau n. Data helm tidak jadi dihapus.")
    except KeyError:
        print("Nomor penitipan tidak ditemukan.")
    input("Tekan Enter untuk kembali...")


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
