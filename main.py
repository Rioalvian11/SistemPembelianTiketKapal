import mysql.connector

conn = mysql.connector.connect(
    host="localhost", port=3306, user="root", password="", database="pbo_project")
cursor = conn.cursor()

if conn.is_connected():
    print("berhasil")


class Customer:
    def lihat_akun(id_customer):
        query = "SELECT * FROM customer WHERE id_customer = {}".format(
            id_customer)
        cursor.execute(query)
        dataTabel = cursor.fetchall()
        for data in dataTabel:
            print(data)

    def regis():
        nama_lengkap = input('Masukkan Nama Lengkap : ')
        jenis_kelamin = input('Masukkan Jenis Kelamin (Pria/Wanita) : ')
        nomor_telepon = input('Masukkan Nomor Telepon : ')
        kota_asal = input('Masukkan Kota : ')
        email = input('Masukkan Email: ')
        username = input('Masukkan Username : ')
        password = input('Masukkan Password : ')
        query = "INSERT INTO customer (nama_lengkap, jenis_kelamin, nomor_telepon, kota_asal, email, username, password) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(
            nama_lengkap, jenis_kelamin, nomor_telepon, kota_asal, email, username, password)
        cursor.execute(query)
        conn.commit()
        print("data berhasil ditambahkan")

    def update_akun(id_customer):
        nama_lengkap = input('Masukkan Nama Lengkap : ')
        jenis_kelamin = input('Masukkan Jenis Kelamin (Pria/Wanita) : ')
        nomor_telepon = input('Masukkan Nomor Telepon : ')
        kota_asal = input('Masukkan Kota : ')
        email = input('Masukkan Email: ')
        username = input('Masukkan Username : ')
        password = input('Masukkan Password : ')
        query = "UPDATE customer SET nama_lengkap = '{}', jenis_kelamin = '{}', nomor_telepon = '{}', kota_asal = '{}', email = '{}', username = '{}', password = '{}' WHERE id_customer = '{}'".format(
            nama_lengkap, jenis_kelamin, nomor_telepon, kota_asal, email, username, password, id_customer)
        print(query)
        cursor.execute(query)
        conn.commit()
        print("data berhasil dirubah")


class Tiket(Customer) :
    def beli_tiket() :
        tanggal_keberangkatan = input('Masukkan Tanggal Keberangkatan : ')
        waktu = int(input('Masukkan Waktu : '))
        jumlah_penumpang = int(input('Masukkan Jumlah Penumpang : '))
        harga = int(input("Masukkan harga tiket : "))
        query = "INSERT INTO data_tiket (tanggal_keberangkatan, waktu, jumlah_penumpang, harga) VALUES ('{}','{}','{}','{}')".format(
            tanggal_keberangkatan, waktu, jumlah_penumpang, harga)
        cursor.execute(query)
        conn.commit()
        print('Terimakasih Telah membeli Tiket')

    def lihat_tiket(id_customer):
        query = "SELECT * FROM data_tiket"
        cursor.execute(query)
        dataTabel = cursor.fetchall()
        for data in dataTabel:
            print(data)
        query_data = "SELECT * FROM data_tiket WHERE id_tiket = '{}'".format(id_customer)
        cursor.execute(query_data)
        dataTabel = cursor.fetchall()
        for data in dataTabel:
            print(data)


def login():
    Email = input("Masukkan Email : ")
    Password = input("Masukkan Password : ")
    cursor = conn.cursor()
    sql = "SELECT * FROM customer WHERE email= %s AND password= %s"
    cursor.execute(sql, (Email, Password))
    results = cursor.fetchall()
    return results[0][0]


id_customer = None

while True:
    print(conn)
    print("Pilihan Menu : \n 1. Lihat Akun \n 2. Ubah Akun \n 3. Beli Tiket \n 4. Lihat Tiket \n 5. Register \n 6. Login \n 7. Keluar")
    pilihan = int(input("Masukkan Pilihan Anda : "))
    if pilihan == 1 and id_customer:
        Customer.lihat_akun(id_customer)
    elif pilihan == 2 and id_customer:
        Customer.update_akun(id_customer)
    elif pilihan == 3 and id_customer:
        Tiket.beli_tiket()
    elif pilihan == 4 and id_customer:
        Tiket.lihat_tiket(id_customer)
    elif pilihan == 5:
        Customer.regis()
    elif pilihan == 6:
        id_customer = login()
    elif pilihan == 7:
        print("Terima kasih")
        break
    else:
        print("Silahkan Masukkan Kembali")
