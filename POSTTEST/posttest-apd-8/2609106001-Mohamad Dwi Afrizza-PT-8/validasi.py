import data


def cek_waktu(waktu):
    waktu_valid = False
    if len(waktu) == 5 and waktu[2] == ".":
        if (waktu[0] in data.angka and waktu[1] in data.angka
                and waktu[3] in data.angka and waktu[4] in data.angka):
            if waktu[0:2] < "24" and waktu[3:5] < "60":
                waktu_valid = True
    return waktu_valid


def cari_jenis(pilih_jenis):
    jenis_dipilih = ""
    no = 1
    for jenis in data.daftar_jenis:
        if pilih_jenis == str(no):
            jenis_dipilih = jenis
        no += 1
    return jenis_dipilih