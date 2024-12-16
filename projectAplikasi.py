kamar_hotel = [
    {"no": 101, "tipe": "single", "harga": 75000},
    {"no": 102, "tipe": "double", "harga": 100000},
    {"no": 103, "tipe": "twin", "harga": 125000},
    {"no": 104, "tipe": "double", "harga": 150000}
]

pesanan_kamar = []

def tampilkan_menu():
    print(40* '=')
    print('Selamat Datang Di BSI Hotel')
    print('1. Lihat Daftar Kamar')
    print('2. Pesan Kamar')
    print('3. Lihat Daftar Pesanan')
    print('4. Keluar')
    
def lihat_daftar_kamar():
    print (40* '=')
    print('Daftar Kamar :')
    for kamar in kamar_hotel:
        print(f"No. {kamar['no']}, Tipe: {kamar['tipe']}, Harga : {kamar['harga']}")
        
def pesan_kamar():
    print (40* '=')
    no_kamar = int(input('Masukkan Nomor Kamar Yang Ingin Anda Pesan : '))
    nama_pemesan = input('Masukkan Nama Pemesan : ')
    jumlah_malam = int(input('Masukkan Jumlah Malam Menginap :'))
    
    kamar_terpilih = None
    for kamar in kamar_hotel:
        if kamar['no'] == no_kamar:
            kamar_terpilih = kamar
            break
    
    if kamar_terpilih == None:
        print ('Maaf, kamar tidak ditemukan')
        return
    
    total_harga = kamar_terpilih['harga'] * jumlah_malam
    
    pesanan_kamar.append({
        "no_kamar" : no_kamar,
        "nama_pemesan" : nama_pemesan,
        "jumlah_malam" : jumlah_malam,
        "total_harga" : total_harga     
    })
    
    print('Pesanan Anda Telah Diterima')
    
def lihat_daftar_pesanan():
    print(40* '=')
    print('Daftar Pesanan')
    for pesanan in pesanan_kamar:
        print(f"No. Kamar : {pesanan['no_kamar']}, Nama Pemesan : {pesanan['nama_pemesan']}, Jumlah Malam : {pesanan['jumlah_malam']}, Total Harga : {pesanan['total_harga']}") 
        
def main():
    while True:
        tampilkan_menu()
        pilihan = int(input(' Masukkan Pilihan Anda : '))
        
        if pilihan == 1:
            lihat_daftar_kamar()
        elif pilihan == 2:
            pesan_kamar()
        elif pilihan == 3:
            lihat_daftar_pesanan()
        elif pilihan == 4:
            break
        else:
            print (40* '=')
            print('Pilihan Tidak Ada')
            
main()