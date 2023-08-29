import math

# Data jumlah pasien yang datang ke rumah sakit dalam beberapa hari
data_pasien = [120, 140, 110, 130, 150]

# Hitung rata-rata
rata_rata = sum(data_pasien) / len(data_pasien)

# Hitung perbedaan kuadrat dan simpan dalam list
perbedaan_kuadrat = [(x - rata_rata)**2 for x in data_pasien]

# Hitung variansi
variansi = sum(perbedaan_kuadrat) / len(data_pasien)

# Hitung standar deviasi (akar kuadrat dari variansi)
standar_deviasi = math.sqrt(variansi)

# Tampilkan hasil
print("Data Jumlah Pasien:", data_pasien)
print("Rata-rata Jumlah Pasien:", rata_rata)
print("Variansi:", variansi)
print("Standar Deviasi:", standar_deviasi)
