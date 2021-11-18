#input
makanan = int(input("Harga makanan sebesar Rp "))
snack   = int(input("Harga snack sebesar Rp "))
minuman = int(input("Harga minuman sebesar Rp "))
uang    = int(input("Uang yang anda bawa sebesar Rp "))

bayar = makanan+snack+minuman
print("Total yang harus anda bayar sebesar Rp" ,bayar)

if bayar > 10000 :
    total = bayar-uang 
    print("Uang anda kurang! Anda memiliki utang sebesar Rp" ,total)

elif bayar == 10000 :
    print("Uang anda pas! Tidak ada kembalian dan utang ")

if bayar < 10000 :
    biaya = uang-bayar
    print("Anda memiliki kembalian sebesar Rp" ,biaya)