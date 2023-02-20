"""
    Bir kelime listesi oluşturulur ve rastgele bir kelime seçilir.
    Ardından kullanıcının tahmin etmesi gereken kelimeyi belirtmek için kullanıcının tahmin edebileceği harf sayısı hesaplanır.
    Oyuncunun tahmin ettiği her harf, doğru veya yanlış olduğuna bağlı olarak,
    ilgili listeye eklenir ve oyuncunun kalan can sayısı azalır. Oyunun sonunda, kullanıcının kazanıp kazanmadığı belirtilir.
"""

import random

kelimler = ("elma", "armut", "cilek", "muz", "portakal", "karpuz")
kelime = random.choice(kelimler)
harf_sayisi = len(kelime)
print("Kelime {} harf içeriyor".format(harf_sayisi))

dogru_harfler = []
yanlis_harfler = list()
can_sayisi = 6

while can_sayisi > 0:
    harf = input("Bir harf girin: ").lower()

    if (len(harf) != 1) or (not harf.isalpha()):
        print("Lutfen sadece bır harf gırınız")
        continue
    if (harf in dogru_harfler) or (harf in yanlis_harfler):
        print("Bu harfi daha oncden girdiniz")
        continue
    if harf in kelime:
        print("Dogru")
        dogru_harfler.append(harf)

        if set(dogru_harfler) == set(kelime):
            print("Tebrikler kazandiniz! Kelime : ", kelime)
            break

        secenek = input("Kelime tahmini yapmak istiyorsaniz q ya basınız \n")
        if secenek == "q":
            tahmin = input("Tahminiz nedir? \n")
            if tahmin == kelime:
                print("Tebrikler kazandiniz! Kelime : ", kelime)
                break
            else:
                print("Yanlış kelime girdiniz")
                can_sayisi -= 1
                print("Kalan can sayisi: ", can_sayisi)
    else:
        print("Yanlıs!")
        yanlis_harfler.append(harf)
        can_sayisi -= 1
        print("Kalan can sayisi: ", can_sayisi)
else:
    print("Kaybettiniz. Kelime: ", kelime)
