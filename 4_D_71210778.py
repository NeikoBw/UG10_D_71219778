bilangan1 = int(input("Masukkan bilangan 1 : "))
bilangan2 = int(input("Masukkan bilangan 2 : "))
bilangan3 = int(input("Masukkan bilangan 3 : "))

if bilangan1>bilangan2>bilangan3 :
    print("Urutan bilangan dari yang terbesar adalah" ,bilangan1 ,bilangan2 ,bilangan3)
elif bilangan1>bilangan3>bilangan2 :
    print("Urutan bilangan dari yang terbesar adalah" ,bilangan1 ,bilangan3 ,bilangan2)
elif bilangan2>bilangan3>bilangan1 :
    print("Urutan bilangan dari yang terbesar adalah" ,bilangan2 ,bilangan3 ,bilangan1)
elif bilangan2>bilangan1>bilangan3 :
    print("Urutan bilangan dari yang terbesar adalah" ,bilangan2 ,bilangan1 ,bilangan3)
elif bilangan3>bilangan2>bilangan1 :
    print("Urutan bilangan dari yang terbesar adalah" ,bilangan3 ,bilangan2 ,bilangan1)
elif bilangan3>bilangan1>bilangan2 :
    print("Urutan bilangan dari yang terbesar adalah" ,bilangan3 ,bilangan1 ,bilangan2)
elif bilangan1==bilangan2>bilangan3 :
    print("Urutan bilangan dari yang terbesar adalah" ,bilangan1 ,bilangan2 ,bilangan3)
elif bilangan1==bilangan3>bilangan2 :
    print("Urutan bilangan dari yang terbesar adalah" ,bilangan1 ,bilangan3 ,bilangan2)
elif bilangan2==bilangan1>bilangan3 :
    print("Urutan bilangan dari yang terbesar adalah" ,bilangan2 ,bilangan1 ,bilangan3)
elif bilangan2==bilangan3>bilangan1 :
    print("Urutan bilangan dari yang terbesar adalah" ,bilangan2 ,bilangan3 ,bilangan1)
elif bilangan3==bilangan1>bilangan2 :
    print("Urutan bilangan dari yang terbesar adalah" ,bilangan3 ,bilangan1 ,bilangan2)
elif bilangan3==bilangan2>bilangan1 :
    print("Urutan bilangan dari yang terbesar adalah" ,bilangan3 ,bilangan2 ,bilangan1)
elif bilangan1>bilangan2==bilangan3 :
    print("Urutan bilangan dari yang terbesar adalah" ,bilangan1 ,bilangan2 ,bilangan3)
elif bilangan2>bilangan3==bilangan1 :
    print("Urutan bilangan dari yang terbesar adalah" ,bilangan2 ,bilangan3 ,bilangan1)
elif bilangan3>bilangan1==bilangan2 :
    print("Urutan bilangan dari yang terbesar adalah" ,bilangan3 ,bilangan1 ,bilangan2)
else :
    print("Tidak Bisa diAplikasikan")

