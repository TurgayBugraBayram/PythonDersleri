# myTuple = ("tuple","dersi","python","tuple")
# print(myTuple)
# print(type(myTuple))
# mylist = ["elma","armut","kivi","karpuz"]
# print(mylist)
# mylist[0] = "üzüm"
# print(mylist)
#
# # tuple[0] = "list"
# # print(mylist)
#
# # tek elamnlı
# myTuple1 = tuple(("demet"))
# #myTuple1  = ("demet",)
# print(type(myTuple1))

# myTuple2 = (1,2,3,4,5)
# print(myTuple2)
#
# myTuple3 = (True,False,True)
# print(myTuple3)
# myTuple4 = (1.5,5.7)
# print(myTuple4)

# myTuple5 = (True,2,"demet",10.6,)
# print(myTuple5)
#
# print(myTuple5[2])



# print(manav[2:5])
# print(manav[::2])
# print(manav[1:5:3])
# print(manav[-1])
# print(len(manav))

manav = ("elma","armut","muz","üzüm","kavun","karpuz","domates")

manavListe = list(manav)
# print(type(manavListe))
manavListe[0] = "biber"
print(manavListe)
manavListe.remove("armut")
manavListe.pop(1)
# manavListe.clear()
print(manavListe)
manav = tuple(manavListe)
# print(type(manav))
del manav

# manav1 = ("elma","salatalik")
# print(manav+manav1)
# print(manav1 +manav)

renkler = ("siyah","sari","kirmizi","mavi","turuncu")
*a,b,c = renkler
print(a)
print(b)
print(c)

print(renkler)

if "mor" in renkler:
    print("siyah var")
else:
    print("mor yok")