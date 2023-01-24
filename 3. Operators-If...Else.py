# print("==", a == b)
# print("!=", a !=b)
# print(">", a > b)
# print("<", a < b)
# print(">=", a >= b)
# print("<=", a<=b)

# print(a==d and c==b)

# print(a==d or c==b)

# print(a is d)
# print(a is not d)
#
# a = 5
# b = 10
# c = 10
# d=5
#
# if a==c:
#     print("a degeri  d degerine eşittir")
# print("if'in dışındayım")

# x = 17
# # y = int(input("Bir sayı giriniz : "))
#
# if x == 10:
#     print("deger 10")
# elif x == 15:
#     print("deger 15")
# else:
#     print("else calisti")

y = input("Bir sayı giriniz : ")
x = input("Bir sayı giriniz : ")

if int(y)==int(x):
    print("eşittir")
elif int(y) > int(x):
    print("y büyük")
else:
    print("x büyük")