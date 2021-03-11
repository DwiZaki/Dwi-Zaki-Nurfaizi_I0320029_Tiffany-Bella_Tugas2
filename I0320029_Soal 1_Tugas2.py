#Menghitung Luas Persegi Panjang
p = float(input("Masukkan p: "))
l = float(input("Masukkan l: "))
luas_persegi_panjang = p * l
print (luas_persegi_panjang)

#Menghitung Luas Lingkaran
r = float(input("Masukkan r (jari-jari lingkaran): "))
pi = 3.14
luas_lingkaran = pi * (r**2)
print (luas_lingkaran)

#Menghitung Luas Kubus
sisi = float(input("Masukkan Panjang rusuk kubus: "))
luas_kubus = 6 * (sisi**2)
print (luas_kubus)

#Konversi Suhu dari Celcius ke Fahrenheit
celcius = float(input("Masukkan suhu (Celcius): "))
konversi_fahrenheit = (9/5 * celcius) + 32
print (konversi_fahrenheit)

#Konversi Suhu dari Reamur ke Kelvin
reamur = float(input("Masukkan suhu (Reamur): "))
konversi_kelvin = (5/4 * reamur) + 273
print (konversi_kelvin)
