usd = 38
eur = 41
tl = 1

kur1 = input("Döviz Kuru Giriniz: ")
kur2 = input("çevireceğimiz Döviz Kurunu Giriniz: ")
bakiye = int(input("Bakiye Giriniz: "))

if kur1 == "tl" and kur2 == "usd":
    sonuc = bakiye / usd
    print("Sonuç: ", sonuc, "Dolar")
elif kur1 == "tl" and kur2 == "eur":
    sonuc = bakiye / eur
    print("sonuç: " + str(sonuc) + " Euro")
elif kur1 == "usd" and kur2 == "tl":
    sonuc = bakiye * usd
    print("Sonuç: ", sonuc, "TL")
elif kur1 == "eur" and kur2 == "tl":
    sonuc = bakiye * eur
    print("Sonuç: ", sonuc, "TL")
elif kur1 == "usd" and kur2 == "eur":
    tl = bakiye * usd
    sonuc = tl / eur
    print("Sonuç: ", sonuc, "Euro")
elif kur1 == "eur" and kur2 == "usd":
    tl = bakiye * eur
    sonuc = tl / usd
    print("Sonuç: ", sonuc, "Dolar")
else:
    print("Yanlış döviz kuru girdiniz.")