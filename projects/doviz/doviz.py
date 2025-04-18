#requests kütüphanesini ekledim
import requests

#veri çekmeye başlayalım
url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_YJCwRKjN5llJ9CGb0jv3dELGNgxuXRe3pKMPgkph"
cevap = requests.get(url)
veri = cevap.json()

#kurlarımızı tanımlayalım ve api üzerinden kurların değerlerini verelim
tl = veri['data'] ['TRY']
eur = veri['data'] ['EUR']
usd = 1

#kullanıcıya hangi döviz üzerinden işlem yapmak istediğini soralım.
while True:
	islem = input("Yapmak istediğiniz işlemi seçiniz 1 (çevirme) 2 (çıkış): ")
	if islem == "1":
		kur1 = input("Merhaba, gerçek zamanlı kur çeviriciye hoş geldiniz. Bana elinizde hangi döviz bulunduğunu söyler misiniz? (tl, eur, usd): ")
		bakiye = int(input("Peki bu elinizdeki dövizin miktarını girer misiniz?: "))
		kur2 = input("Hangi dövize çevirmek istersiniz?: ")

#işlemlerimizi yapalım.
		if kur1 == "usd" and kur2 == "tl":
			net = bakiye * tl
			print("Kur çevrildi. sizin " + str(round(net, 2)) + " TL'niz var")
		elif kur1 == "usd" and kur2 == "eur":
			net = bakiye / eur
			print("Kur çevrildi. Sizin " + str(round(net, 2)) + " Euro'nuz var.")
		elif kur1 == "eur" and kur2 == "usd":
			net = bakiye / eur
			print("Kur çevrildi. Sizin " + str(round(net, 2)) + " Dolar'ınız var.")
		elif kur1 == "eur" and kur2 == "tl":
			usd = bakiye * eur
			net = usd * tl
			print("Kur çevrildi. Sizin " + str(round(net, 2)) + " TL'niz var.")
		elif kur1 == "tl" and kur2 == "usd":
			net = bakiye / tl
			print("Kur çevrildi. Sizin " + str(round(net, 2)) + " Dolar'ınız var.")
		elif kur1 == "tl" and kur2 == "eur":
			usd = bakiye / tl
			net = usd / eur
			print("Kur çevrildi. Sizin " + str(round(net, 2)) + " Euro'nuz var.")
		else:
			print("Böyle bir kur halihazırda eklenmemiş veya bulunmayabilir. Lütfen bulunduğundan eminseniz bizimle iletişime geçin. Emin değilseniz buyrun tekrar deneyin. ")

	elif islem == "2":
		print("Çıkışınız sağlandı. Güle Güle :)")
		break
