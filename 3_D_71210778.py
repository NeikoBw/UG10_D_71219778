barang1, barang2, barang3 = list(input("Masukkan daftar belanja Anda : ").split(", "))
f = barang1.title()
t = barang2.title()
i = barang3.title()

print("Daftar belanja : ['"+f+"', '"+t+"', '"+i+"']")
proses = input("Masukkan barang yang ingin ditambahkan : ")
prosesx = proses.title()
x = prosesx.upper()

if prosesx == f:
    print("Daftar belanja", x,"sudah berada dalam daftar belanja")
elif prosesx == t:
    print("Daftar belanja", x,"sudah berada dalam daftar belanja")
elif prosesx == i:
    print("Daftar belanja", x,"sudah berada dalam daftar belanja")
else:
    print("Hasil penambahan pada daftar belanja : ['"+f+"', '"+t+"', '"+i+"', '"+x+"']")