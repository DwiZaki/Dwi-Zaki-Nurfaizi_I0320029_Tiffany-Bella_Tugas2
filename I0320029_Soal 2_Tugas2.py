#Data
nama = "Dwi Zaki Nurfaizi"
jenis_kelamin = "laki-laki"
alamat = "Jl. Stasiun I No. 74, Bantarsoka, Purwokerto Barat, Banyumas"
tinggi_badan = 171
hobi = "main basket"
makanan_favorit = "nasi goreng"
minuman_favorit = "minuman rasa coklat"
berat_badan = 54
ukuran_sepatu = 43
ukuran_sepatu_cm = 26.8
pekerjaan = "mahasiswa"
prodi = "Teknik Industri"
univ = "Universitas Sebelas Maret"
angkatan = 2020

#Umur
import datetime
date = datetime.datetime.now()

tanggal_lahir = 8
bulan_lahir = 6
tahun_lahir = 2002

umur_dalam_bulan = (date.year - tahun_lahir) * 12 + (date.month - bulan_lahir) + (date.day - tanggal_lahir)/30
umur_dalam_tahun = umur_dalam_bulan / 12
umur_dalam_hari = umur_dalam_bulan * 30

#Output
print (Profil singkat saya sebagai berikut :)
print (nama)
print (jenis_kelamin)
print (alamat)
print (tinggi_badan, "cm")
print (hobi)
print (makanan_favorit)
print (minuman_favorit)
print (berat_badan, "kg")
print (ukuran_sepatu)
print (ukuran_sepatu_cm, "cm")
print (pekerjaan)
print (prodi)
print (univ)
print (angkatan)

#Menceritakan diri
print ("Perkenalkan namaku", nama, "aku berjenis kelamin", jenis_kelamin "aku tinggal di", alamat, "umurku", umur_dalam_tahun, "tahun", umur_dalam_bulan, "bulan", umur_dalam_hari, "hari. Tinggiku", tinggi_badan, "cm. Hobiku", hobi, "makanan dan minuman favoritku yaitu", makanan_favorit, "dan", minuman_favorit, "\nAku merupakan seorang", pekerjaan, prodi, univ, "angkatan", angkatan)
