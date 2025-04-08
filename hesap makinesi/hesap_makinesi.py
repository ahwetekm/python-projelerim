islem = input("Hesaplamak istediğiniz işlemi girin (+, -, *, /): ")
sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

if islem == "+":
    sonuc = sayi1 + sayi2
    print("Toplama işlemi başarılı. " + str(sonuc))
elif islem == "-":
    sonuc = sayi1 - sayi2
    print("Çıkarma işlemi başarılı. " + str(sonuc))
elif islem == "*":
    sonuc = sayi1 * sayi2
    print("Çarpma işlemi başarılı. " + str(sonuc))
elif islem == "/":
    sonuc = sayi1 / sayi2
    print("Bölme işlemi başarılı. " + str(sonuc))
else:
    print("Geçersiz işlem girdiniz.")