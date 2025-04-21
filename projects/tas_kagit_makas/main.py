"""
1 = taş
2 = kağıt
3 = makas
"""
import random
print("Merhaba, oyunuma hoş geldiniz.")
print("oyun basit. siz bana hangi hamleyi oynayacağınızı söyleyeceksiniz. ben ise sizinle oynayacağım. BOL ŞANS çünkü çok ihtiyacınız olacak.")
print("hamlelerden bahsedeyim. 1[taş] 2[kağıt] 3[makas]")
skor = 0

def hamle():
    global skor
    print("Hamlenizi alayım:")
    hamlesi = input()
    hamlemiz = random.randint(1, 3)
    if hamlesi == "1" and hamlemiz == 1:
        print("(Sen taş yaptın ve ben de taş yaptım)")
        print("Taşa taş mı? berabere, devam edelim")    
        hamle()
    elif hamlesi == "1" and hamlemiz == 2:
        print("(sen taş yaptın ve ben kağıt yaptım)")
        print("Kağıt yaptım ve kazandım. Muhahahahaaa ben kazandımm. semi yenmek seriden keyifli.devam ediyoruz")
        skor = skor - 1
        hamle()
    elif hamlesi == "1" and hamlemiz == 3:
        print("(sen taş yaptın ve ben de makas yaptım)")
        print("makası kim icat etti? acemi şansı devam edelim")
        skor = skor + 1
        hamle()
    elif hamlesi == "2" and hamlemiz == 1:
        print("sen kağıt yaptın ve ben de taş yaptım")
        print("taşı kim icat etti? lanet olsunnnn")
        skor = skor + 1
        hamle()
    elif hamlesi == "2" and hamlemiz == 2:
        print("(sen kağıt yaptın ve ben de kağıt yaptım)")
        print("benşmle aynı şeyleri yapmayı bırak")
        hamle()
    elif hamlesi == "2" and hamlemiz == 3:
        print("(sen kağıt yaptın ve ben de makas yaptım)")
        print("muhahahahaha bu işi bırakmalısın")
        skor = skor - 1
        hamle()
    elif hamlesi == "3" and hamlemiz == 1:
        print("(sen makas yaptın ve ben de taş yaptım)")
        print("muahhahahaha")
        skor = skor - 1
        hamle()
    elif hamlesi == "3" and hamlemiz == 2:
        print("(sen makas yaptın ve ben de kağıt yaptım)")
        print("acemi şansıııı")
        skor = skor + 1
        hamle()
    elif hamlesi == "3" and hamlemiz == 3:
        print("(sen makas yaptın ve ben de makas yaptım)")
        print("bilader bir daha benimle aynı şeyleri yapma")
        hamle()
    elif hamlesi == "0":
        print("gidiyorsun demek. korkaksın")
        print("Skorun: " + str(skor))
    else:
        print("Hey hey hey bu geçersiz bir hamle. tekrar denemelisin")
        hamle()

hamle()


