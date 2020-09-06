#import date & time
import datetime

# Variabel array global untuk menyimpan data
kursi = []
status = []
tanggal = []


# fungsi untuk menampilkan semua denah
def show_data():
    if len(kursi) <= 0:
        print("\t========== Laporan Denah =============\n")
        print("|No |", "|===== Kursi =====|", "|==== Status ====|")
        print("\n\tBELUM ADA DATA")
    else:
        print("\t========== Laporan Denah =============\n")
        print("|No |", "|===== Kursi =====|", "|==== Status ====|")
        for indeks in range(len(kursi)):
            print("|", indeks + 1, "| |      ", kursi[indeks],
                  "       | |     ", status[indeks], "     |")


# fungsi untuk menampilkan denah transaksi
def transaction_data():
    if len(kursi) <= 0:
        print("\t========== Laporan Denah Transaksi =============")
        print("|No |", "|===== Kursi =====|", "|==== Tanggal Transaksi ====|")
        print("\n\tbelum ada transaksi")
    else:
        print("\t========== Laporan Denah Transaksi =============\n")
        print("|No |", "|===== Kursi =====|",
              "|========== Tanggal Transaksi ===========|")
        for indexs in range(len(kursi)):
            print("|", indexs + 1, "| |      ", kursi[indexs],
                  "       | |     ", tanggal[indexs], "       |")


# fungsi untuk menambah pemesanan kursi
def insert_data():
    print("Contoh Kode kursi [A1,A2,A3,A4,A5]\n")
    kursi_baru = input("Masukan Kode kursi: ")
    status_kursi = input("Status kursi?[sold/free] :")
    tgl_pemesanan = datetime.datetime.now()
    kursi.append(kursi_baru)
    status.append(status_kursi)
    tanggal.append(tgl_pemesanan)


# fungsi untuk edit pemesanan kursi
def edit_data():
    show_data()
    indeks = int(input("Inputkan No kursi: ")) - 1
    if (indeks >= len(kursi)):
        print("Kursi Belum dipesan")
    else:
        pesan_baru = input("pesan kursi baru: ")
        status_baru = input('ubah status: ')
        kursi[indeks] = pesan_baru
        status[indeks] = status_baru


# fungsi untuk membatalkan pesanan
def delete_data():
    show_data()
    indeks = int(input("Inputkan No kursi: ")) - 1
    if (indeks >= len(kursi)):
        print("Kursi Masih kosong")
    else:
        kursi.remove(kursi[indeks])
        status.remove(status[indeks])
        tanggal.remove(tanggal[indeks])


# fungsi untuk menampilkan menu
def show_menu():
    print("\n")
    print(
        "=========== Selamat Datang (Cinema XXI), Silahkan masukan konfigurasi denah studio ============\n"
    )

    print("\t\t\t============= Pilih Menu ==============")
    print("[1] Pemesanan kursi --> book_seat")
    print("[2] Batalkan Pesanan --> cancel_seat")
    print("[3] Edit Pesanan kursi --> edit_seat")
    print("[4] Laporan Denah --> seat_status")
    print("[5] Laporan Denah Transaksi --> transaction_status")
    print("[6] Keluar Aplikasi --> exit")

    menu = int(input("MASUKAN MENU: "))
    print("\n")

    if menu == 1:
        insert_data()
    elif menu == 2:
        delete_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        show_data()
    elif menu == 5:
        transaction_data()
    elif menu == 6:
        exit()
    else:
        print("Salah pilih! Menu tidak ada, ulangi....")


# pemamnggilan main show menu
if __name__ == "__main__":

    while (True):
        show_menu()