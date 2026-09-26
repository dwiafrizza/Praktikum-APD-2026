print("=== SISTEM KASIR BIOSKOP XXI ===")

nama = input("Nama pembeli: ")
umur = int(input("Umur pembeli: "))

if umur < 13:
    print("Mohon maaf, anda belum cukup umur untuk menonton")

else:
    jenis_tiket = input("Jenis tiket (Reguler/Premium/VIP): ")

    if jenis_tiket == "Reguler":
        harga_tiket = 50000
    elif jenis_tiket == "Premium":
        harga_tiket = 75000
    elif jenis_tiket == "VIP":
        harga_tiket = 100000
    else:
        harga_tiket = 0
        print("Jenis tiket tidak valid")

    if harga_tiket != 0:
        status_member = input("Status member (Ya/Tidak): ")

        if status_member == "Ya":
            keterangan_member = "Member"
        elif status_member == "Tidak":
            keterangan_member = "Bukan Member"
        else:
            keterangan_member = "Tidak Valid"
            print("Status member tidak valid")

        if keterangan_member != "Tidak Valid":
            uang_bayar = int(input("Nominal uang bayar: "))

            diskon = harga_tiket * 20 / 100 if status_member == "Ya" else 0
            biaya_admin = 0 if status_member == "Ya" else 2000

            total_bayar = harga_tiket - diskon + biaya_admin

            if uang_bayar < total_bayar:
                print("Uang bayar kurang dari total bayar")

            else:
                kembalian = uang_bayar - total_bayar

                print()
                print("=== STRUK PEMBELIAN ===")
                print("Nama Pembeli :", nama)
                print("Umur         :", umur)
                print("Jenis Tiket  :", jenis_tiket)
                print("Status Member:", keterangan_member)
                print("Harga Tiket  :", harga_tiket)
                print("Diskon       :", diskon)
                print("Biaya Admin  :", biaya_admin)
                print("Total Bayar  :", total_bayar)
                print("Uang Bayar   :", uang_bayar)
                print("Kembalian    :", kembalian)
                print("=======================")
                print("Terima kasih telah membeli tiket")
                print("di Bioskop XXI!")
                print("Selamat menikmati film.")