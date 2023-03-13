def seslisesizharfsayısı(metin):
    # Kullanıcıdan bİr metin girmesini isteyen ve girilen bu metinde bulunan sesli-sessiz harflerin sayısını ekranda
    sesli_harfler = ["a", "e", "i", "ı", "o", "ö", "u", "ü"]
    sesli_sayisi = 0
    sessiz_sayisi = 0

    for harf in metin:
        if harf.isalpha():
            if harf.lower() in sesli_harfler:
                # sesli_sayisi = sesli_sayisi +1
                sesli_sayisi += 1
            else:
                sessiz_sayisi += 1
    print("Sesli harf sayısı : ", sesli_sayisi)
    print("Sessiz harf sayısı: ", sessiz_sayisi)


# metin = input("Bir metin girin : \n ")
# seslisesizharfsayısı(metin)


def fibonacci():
    n = int(input("Kac adet fibbonaci sayisi yazilsin: "))  # 0 1 1 2 3 5 8
    # sayi1 = 0
    # sayi2 = 1
    sayi1, sayi2 = 0, 1
    if n == 1:
        print(sayi1)
    elif n == 2:
        print(sayi1, sayi2)
    else:
        print(sayi1, sayi2, end=" ")
        for i in range(n - 2):
            sayi3 = sayi1 + sayi2
            print(sayi3, end=" ")
            sayi1, sayi2 = sayi2, sayi3


# fibonacci()


def atm():
    bakiye = 500
    while 1:
        print("""
            İşlemler:

            1. Bakiye Sorgulama
            2. Para Yatırma
            3. Para Çekme

            Programdan 'q' tuşu ile çıkabilirsiniz.
            """)
        işlem = input("İşlemi giriniz: ")

        if işlem == "q":
            print("güle güle")
            break
        elif işlem == "1":
            print(f"Bakiyeniz {bakiye} liradir")
        elif işlem == "2":
            miktar = float(input("Tutar: "))
            bakiye += miktar
        elif işlem == "3":
            miktar = float(input("Tutar: "))
            if (bakiye - miktar) < 0:
                print(f"{miktar} kadar para çekmezsiniz")
                print(f"Bakiyeniz {bakiye} liradir")
                continue
            bakiye -= miktar
        else:
            print("Hatalı İşlem")
atm()
