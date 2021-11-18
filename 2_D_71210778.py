a = int(input("Nilai a : "))
b = int(input("Nilai b :"))
c = int(input("Nilai c :"))

D = (b*b) - (4*a*c)
x1 = (-b + D / 2) / 2*a
x2 = (-b - D / 2) / 2*a

if D<0 :
    print("Fungsi tersebut tidak memiliki akar riil")
elif D>0 :
    print("Akar akar dari persamaan tersebut adalah" ,x2,"dan",x1)
else :
    D==0 
    print("Fungsi tersebut memiliki akar kembar yaitu" ,x1)
