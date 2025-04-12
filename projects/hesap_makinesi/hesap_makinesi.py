sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))
islem = input("Yapmak istediğiniz işlemi seçiniz  (+, -, /, *,): ")
if islem == "+":
    sonuc = sayi1 + sayi2
    print("Toplama işlemini seçtiniz. Sonuç: " + str(sonuc))
elif islem == "-":
    sonuc = sayi1 - sayi2
    print("Çıkartma işlemini seçtiniz. Sonuç: " + str(sonuc))
elif islem == "/":
    sonuc = sayi1 / sayi2
    if syi2 == 0:
        print("Hiçbir sayı sıfıra bölünmez.")
    else:
        print("Bölme işlemini seçtiniz. Sonuç: " + str(sonuc))
elif islem == "*":
    sonuc = sayi1 * sayi2
    print("Çarpma işlemini seçtiniz. Sonuç: " + str(sonuc))
else:
    print("Geçersiz işlem girdisi. Lütfen geçerli bir girdi giriniz.")