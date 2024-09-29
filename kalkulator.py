print(30*"=")
print('Selamat Datang Di BSI Kalkulator')
print(30*"=")

#angka nya

angka_1 = float(input('Masukkan Angka Ke-1 : '))
operator = input('Pilih operator nya : | + | - | x | / |  :  ')
angka_2 = float(input('Masukkan Angka Ke-2 : '))

#pencabangannya

if operator == "+":
    hasil = angka_1 + angka_2
    print (f'Hasilnya adalah : {hasil}')
elif operator == "-":
    hasil = angka_1 - angka_2
    print (f'Hasilnya adalah : {hasil}')
elif operator == "x":
    hasil = angka_1 * angka_2
    print (f'Hasilnya adalah : {hasil}')
elif operator == "/":
    hasil = angka_1 / angka_2
    print (f'Hasilnya adalah : {hasil}')
    




