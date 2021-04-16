str = "Selamat Datang di Toko Buah Mixxiw"
s = str.center(50,'*')
print(s)
salam = "Untuk kenyamanan dalam berbelanja, silakan cek ketersediaan buah yang anda cari."
print(salam)

str = input("Masukkan nama anda: ")
nama = str.upper()
print("Hi,",nama+"!")

buah = "Toko kami menyediakan: Lemon, Nanas, Kurma, Rambutan, Jeruk, Melon, Lemon, Kurma, Nanas, Jeruk, Apel, Sirsak,Jeruk, Semangka, Nanas, Rambutan, Pepaya, Anggur, Strawberry, dan Melon "
print(buah)
cari = input("Buah apa yang anda cari?: ")
cari2 = cari.capitalize()
hasil = buah.count(cari2)
print("Persediaan buah",cari2,"di toko kami adalah: ",hasil,"buah")
if hasil>=1:
    print("Selamat berbelanja!")
else:
    print("Mohon maaf,",nama+".","Persediaan buah",cari2,"di toko kami, saat ini kosong.")
