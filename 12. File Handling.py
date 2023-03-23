file = open("isimler.txt", "w")


# file = open("C:/Users/Turgay Bugra/Desktop/deneme.txt")

# file.write("Turgay Bugra\n")
#
# file = open("isimler.txt","a")
#
file.write("Selma\n")
file.write("altun\n")
file.write("ahmet\n")
file.write("fatma\n")
#
#
# try:
#     file = open("isimler.txt", "r")
# except FileNotFoundError:
#     print("dosya bulunamadı...")
# for i in file:
#     print(i,end="")
# print(file.read())
# print("*********")
# veri = file.read()
# print(veri)
# print("bitti")
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print("*************")
# print(file.readline())
# print(file.readlines())
# file.close()

# with open("isimler.txt","r") as file:
#     print(file.tell())
#     file.seek(10)
#     print(file.tell())
#     print(file.read(20))
#     print(file.tell())
# print(file.readline())

with open("isimler.txt","r+") as file:
    liste= file.readlines()
    liste.insert(3, "fatma\n")
    file.seek(0)
    # for satır in liste:
    #     file.write(satır)
    file.writelines(liste)
    file.seek(0)
    print(file.read())
    # veri = file.read()
    # veri = "dosyanın basi" + veri
    # file.seek(0)
    # file.write(veri)

open("deneme.txt","x")

"""
a+==r+==w+
"""
