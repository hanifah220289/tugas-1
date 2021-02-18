#Buatlah sebuah program yang dapat menghitung luas lingkaran.
#Program meminta input dari user berupa angka sebagai jari-jari lingkaran.
#Program menghitung luas lingkaran dengan rumus πr²
#Π = 22/7
#r = jari - jari lingkaran
#Lalu tampilkan ke layar dengan format:
#Hint: untuk menampilkan tanda kuadrat gunakan print(“\u00b2”)
#Luas lingkaran dengan jari-jari [ jari-jari lingkaran ] cm adalah [ luas lingkaran ] cm ² .
#Contoh:
#Luas lingkaran dengan jari-jari 7 cm adalah 154.0 cm ² .
#Luas lingkaran dengan jari-jari 10 cm adalah 314.2857142857143 cm ² .
#Bonus : Ubahlah format luas menjadi 2 angka dibelakang koma
#Hint: Ubah string format untuk float menjadi {:.2f}
#Luas lingkaran dengan jari-jari 10 cm adalah 314.29 cm ² .

jari2= input("masukkan jari2: ")
r = int(jari2)
phi = 22/7
luas = float (phi*r*r)
#luas = {:.2f}
#print (luas)
print ("luas lingkaran dengan jari-jari", r, "cm adalah", luas, "cm²")
hasil = " luas lingkaran dengan jari-jari {} cm adalah {:.2f} cm\u00b2"
print (hasil.format (r, luas))