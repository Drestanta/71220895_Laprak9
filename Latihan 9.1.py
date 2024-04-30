def cari_nilai_terbaik(data):
    data_urut = sorted(data, reverse=True)
    nilai_terbaik = data_urut[:3]
    return nilai_terbaik

data = [25, 12, 33, 7, 19, 20, 1, 15, 18]

nilai_terbaik = cari_nilai_terbaik(data)
print("Tiga nilai terbaik:", nilai_terbaik)
