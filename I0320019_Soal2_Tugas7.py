print("Selamat Datang! Silakan masukkan data yang diperlukan untuk menentukan kelulusan semester ini.")

nama = str(input("Masukkan nama anda: "))
data = []
nilai1 = float(input("Masukkan nilai ujian anda ke- 1: "))
nilai2 = float(input("Masukkan nilai ujian anda ke-2: "))
nilai3 = float(input("Masukkan nilai ujian anda ke-3: "))
databaru = data.append(nilai1)
databaru2 = data.append(nilai2)
databaru3 = data.append(nilai3)
print("Berikut adalah rangkuman nilai anda di semester ini:", data)
ratarata = (nilai1+nilai2+nilai3)/3

import math
rata2 = math.ceil(ratarata)
print("Hi,", nama+"!", "Hasil rata-rata anda adalah:", rata2)

nmax = max(data)
nmin = min(data)

print("Nilai tertinggi anda adalah :", nmax)
print("Nilai terendah anda adalah:", nmin)

if rata2>=70:
    print("Selamat,",nama+"! Anda telah lulus ujian semester ini. Goodluck di semester selanjutnya!")
else:
    print("Mohon maaf,",nama+". Anda harus mengulang ujian karena nilai belum mencukupi rata-rata.")