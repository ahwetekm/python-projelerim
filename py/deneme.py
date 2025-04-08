isim = input("Merhaba, basit mesai hesaplama yazılımına hoş geldiniz. Çalışanın ismini giriniz: ")
measi = int(input("çalışanın kaç sata mesai yaptığını giriniz: "))
mu = int(input("çalışan saatlik ne kadar ücret alıyor: "))
maas = int(input("çalışanın maaşını giriniz: "))

toplam = mu * measi + maas
print( str(isim) + " Adlı çalışanınızın net maşaı: " + str(toplam))
