# def myFunction():
#     print("hello python")
#
#
# def myFunction1():
#     print("a")
#     print("fonksiyon dışı")
#
#
# def araba(renk, marka, yılı):
#     print("rengi: ", renk)
#     print("marka: ", marka)
#     print("yılı: ", yılı)
#
#
# araba("turuncu", "toyota", 2010)
#
# def toplama(a,b,c):
#     print("Toplamlari: " , a+b+c)
#
# toplama(7,8,9)


# def faktoriyel(sayi):
#     faktoriyel = 1
#     if (sayi == 0 or sayi == 1):
#         print("Faktoriyel : ", faktoriyel)
#     else:
#         while sayi > 1:
#             faktoriyel *= sayi
#             sayi -= 1
#         print("Faktoriyel : ", faktoriyel)
#
# user = int(input("Bir sayi giriniz: "))
# faktoriyel(user)

# def selamla(isim = "isimsiz"):
#     print("Selam ", isim)
# selamla()
#
# def showInfo(name="isim yok",surname="soyisim yok",no="no yok"):
#     print("ad: ", name,"soyad: ", surname,"no: ",no)
# showInfo("bugra","turgay",10)
# showInfo(no = 10,surname="turgay")

# def toplama(*parametreler):
#     sum = 0
#     for i in parametreler:
#         sum+=i
#     print(sum)
# toplama(1,2,3,4,5,6,7,8,9)

def toplam(a,b,c):
    return a+b+c
def iki_ile_carp(a):
    return a*2

sum1 = toplam(2,7,8)
print(iki_ile_carp(sum1))
