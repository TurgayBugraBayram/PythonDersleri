# while

# i = 1
# break
# while i < 10:
#     print(i)
#     # i=i+1
#     i += 1
#     if i == 5:
#         break

# i = 0
# continue
# while i < 10:
#     i += 1
#     if i == 5:
#         continue
#     print(i)

# else while
# i= 1
# while i < 10:
#     print(i)
#     i+=1
# else:
#     print("i degerim 10dan büyük değil")

# myList = [1, 2, 3, 4, 5]
# i = 0
# a = "merhaba "
# while i < len(myList):
#     print(a + "indeks:", i, "eleman:", myList[i])
#     i += 1


# for

# print("x" in "merhaba")

# manav = ["elma","armut","mandilana","karpuz","kivi"]
#
# for meyve in manav:
#     print("yiyceklerim", meyve)
#     if meyve == "mandilana":
#        continue
#     print("continue çalışmadı")

# for x in "elma":
#     print(x)

# for i in range(10):
#     print(i)
# for i in range(2,10):
#     print(i)
# for i in range(2,10,3):
#     print(i)
#
# a = input("sayi giriniz: ")
# b = input("sayi giriniz: ")
# c = input("sayi giriniz: ")
#
# for i in range(int(b), int(a),int(c)):
#     print(i)
# print(i)

# for x in range(6):
#     print(x)
# else:
#     print("dongu bitti")
#
# manav = ["elma","armut","mandilana","karpuz","kivi"]
#
# sayi = 5
# for a in manav:
#     pass

# a =1
# while a:
#     sayi = 5
#     print("merhaba")
#     if sayi == 5:
#         a=0

user = input()
user_Check = bool(user)
while bool(user):
    print("çalştı")
else:
    print("calimadi")