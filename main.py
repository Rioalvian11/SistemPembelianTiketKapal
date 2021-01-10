import mysql.connector

conn = mysql.connector.connect(
    host="localhost", port=3306, user="root", password="", database="pbo_projectt")
cursor = conn.cursor()

if conn.is_connected():
    print("berhasil")


class Customer:
    def custom(self, nama_lengkap, jenis_kelamin, nomor_telepon, kota_asal, email, username, password):
        self.nama_lengkap = nama_lengkap
        self.jenis_kelamin = jenis_kelamin
        self.nomor_telepon = nomor_telepon
        self.kota_asal = kota_asal
        self.email = email
        self.username = username
        self.password = password

    def lihat_akun(id_customer):
        query = "SELECT * FROM customer WHERE id_customer = {}".format(id_customer)
        cursor.execute(query)
        dataTabel = cursor.fetchall()
        for data in dataTabel:
            print("ID Customer   : ", data[0])
            print("Nama          : ", data[1])
            print("Jenis Kelamin : ", data[2])
            print("Nomor Telepon : ", data[3])
            print("Kota          : ", data[4])
            print("Email         : ", data[5])
            print("Username      : ", data[6])
            print("Password      : ", data[7])
            break

    def regis(self):
        query = "INSERT INTO customer (nama_lengkap, jenis_kelamin, nomor_telepon, kota_asal, email, username, password) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(
            self.nama_lengkap, self.jenis_kelamin, self.nomor_telepon, self.kota_asal, self.email, self.username, self.password)
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
        cursor.execute(query)
        conn.commit()
        print("data berhasil dirubah")


class Tiket(Customer) :
    def tiket(self, tanggal_keberangkatan, waktu, jumlah_penumpang):
        self.tanggal_keberangkatan = tanggal_keberangkatan
        self.waktu = waktu
        self.jumlah_penumpang = jumlah_penumpang

    def beli_tiket(self) :
        harga = self.jumlah_penumpang * 30000
        query = "INSERT INTO data_tiket (tanggal_keberangkatan, waktu, jumlah_penumpang, harga) VALUES ('{}','{}','{}','{}')".format(
            self.tanggal_keberangkatan, self.waktu, self.jumlah_penumpang, harga)
        cursor.execute(query)
        conn.commit()
        print('Terimakasih Telah membeli Tiket')

    def lihat_tiket(id_customer):
        query = "SELECT * FROM data_tiket"
        cursor.execute(query)
        dataTabel = cursor.fetchall()
        for data in dataTabel:
            print("ID Tiket              : ", data[4])
            print("Tanggal Keberangkatan : ", data[0])
            print("Waktu                 : ", data[1])
            print("Jumlah Penumpang      : ", data[2])
            print("Harga                 : ", data[3])



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
    Customer1 = Customer()
    Tiket1 = Tiket()
    print("=====SELAMAT DATANG DI SIPTIKA=====")
    print("Pilihan Menu : \n 1. Lihat Akun \n 2. Ubah Akun \n 3. Beli Tiket \n 4. Lihat Tiket \n 5. Register \n 6. Login \n 7. Keluar")
    pilihan = int(input("Masukkan Pilihan Anda : "))
    if pilihan == 1 and id_customer:
        Customer.lihat_akun(id_customer)
    elif pilihan == 2 and id_customer:
        Customer.update_akun(id_customer)
    elif pilihan == 3 and id_customer:
        Tiket1.tiket(
        input('Masukkan Tanggal Keberangkatan : '),
        int(input('Masukkan Waktu : ')),
        int(input('Masukkan Jumlah Penumpang : '))
        )
        Tiket1.beli_tiket()
    elif pilihan == 4 and id_customer:
        Tiket.lihat_tiket(id_customer)
    elif pilihan == 5:
        Customer1.custom(
        input('Masukkan Nama Lengkap : '),
        input('Masukkan Jenis Kelamin (Pria/Wanita) : '),
        input('Masukkan Nomor Telepon : '),
        input('Masukkan Kota : '),
        input('Masukkan Email: '),
        input('Masukkan Username : '),
        input('Masukkan Password : ')
        )
        Customer1.regis()
    elif pilihan == 6:
        id_customer = login()
    elif pilihan == 7:
        print("Terima kasih")
        break
    else:
        print("Silahkan Masukkan Kembali")
