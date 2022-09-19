# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Menginput Satuan Jarak
Meter = float(input("Tuliskan Berapa Meter: "))

# Mengkonversi
inch  = Meter * 39.37
kaki  = Meter * 3.280
yard = Meter * 1.09
cm = Meter * 100
 
# Menampilkan Hasil 
print('%0.2f  Meter sama dengan %0.2f Inch' %(Meter,inch))
print('%0.2f  Meter sama dengan %0.2f Kaki' %(Meter,kaki))
print('%0.2f  Meter sama dengan %0.2f Yard' %(Meter,yard))
print('%0.2f  Meter sama dengan %0.2f Centimeter' %(Meter,cm))
