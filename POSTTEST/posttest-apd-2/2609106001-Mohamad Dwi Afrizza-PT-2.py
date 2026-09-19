barang_1 = 15000
barang_2 = 25000
barang_3 = 10000
barang_4 = 5500
barang_5 = 5000
barang_6 = 20000
print("barang_1:", barang_1)
print("barang_2:", barang_2)
print("barang_3:", barang_3)
print("barang_4:", barang_4)
print("barang_5:", barang_5)
print("barang_6:", barang_6)

barang = [barang_1, barang_2, barang_3, barang_4, barang_5, barang_6]
print("list barang:", barang)

total_belanja = barang_1 + barang_2 + barang_3 + barang_4 + barang_5 + barang_6
print("Total belanja: Rp", total_belanja)

pajak = total_belanja * 15 / 100
print("Pajak 15%: Rp", pajak)

total_bayar = total_belanja + pajak
print("Total bayar: Rp", total_bayar)

rata_rata = total_bayar / len(barang)
print("Rata-rata belanja per barang: Rp", rata_rata)

nim = 1
print("NIM:", nim)

bolean = nim < rata_rata
print("Bolean:", bolean)

kurs_usd = 16500
print("Kurs USD:", kurs_usd)

total_usd = total_bayar / kurs_usd
print("total dalam USD:", total_usd)

kurs_myr = 3900
print("Kurs MYR:", kurs_myr)

total_myr = total_bayar / kurs_myr
print("Total dalam MYR:", total_myr)

barang_pilihan = barang[0:5:2]
print("Barang pilihan:", barang_pilihan)

