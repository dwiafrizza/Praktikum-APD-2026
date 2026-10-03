username_benar = "Afrizza"
password_benar = "001"
pin_benar = "001001"
saldo = 5000000

login_berhasil = False

for i in range(3):
    print("=== LOGIN BANK DIGITAL ===")
    username = input("Username : ")
    password = input("Password : ")

    if username == username_benar and password == password_benar:
        login_berhasil = True
        print("Login berhasil!")
        break
    elif username != username_benar and password != password_benar:
        print("Username dan Password anda salah")
    elif username != username_benar:
        print("Username anda salah")
    else:
        print("Password anda salah")

if login_berhasil == False:
    print("Anda gagal login 3x. Akun diblokir!")
else:
    akun_diblokir = False

    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Transfer Uang")
        print("2. Logout")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            transfer_lagi = "y"

            while transfer_lagi == "y":
                print("\n=== TRANSFER UANG ===")
                print(f"Saldo saat ini : Rp{saldo}")
                penerima = input("Username penerima : ")

                while True:
                    nominal = int(input("Nominal transfer : "))

                    if nominal < 50000:
                        print("Nominal minimal Rp50000!")
                    elif nominal > 1000000:
                        print("Nominal maksimal Rp1000000!")
                    elif nominal > saldo:
                        print("Nominal melebihi saldo!")
                    else:
                        break

                pin_valid = False

                for i in range(3):
                    pin = input("Masukkan PIN : ")
                    if pin == pin_benar:
                        pin_valid = True
                        break
                    print("PIN salah!")

                if pin_valid == False:
                    print("Kesempatan habis. Akun diblokir!")
                    akun_diblokir = True
                    break

                saldo = saldo - nominal
                print("\n=== STRUK BUKTI TRANSFER ===")
                print("Username Pengirim :", username_benar)
                print("Username Penerima :", penerima)
                print("Nominal Transaksi : Rp", nominal)
                print("============================")

                transfer_lagi = input("Apakah pengguna ingin melakukan transfer lagi (y/n)? ")

            if akun_diblokir == True:
                break

        elif pilihan == "2":
            print("Logout berhasil. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")