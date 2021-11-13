a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))

if a > b > c:
    print("Bilangan Pertama Adalah Bilangan Terbesar = %s" % a)
elif b > c:
    print("Bilangan kedua adalah bilangan terbesar = %s" % b)
else:
    print("Bilangan ketiga adalah bilangan terbesar = %s" % c) 