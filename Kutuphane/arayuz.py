from modul import *

print ("""
İşlemler : 

1 - Kitapları Listeleme
2 - Kitap Sorgulama
3 - Kitap Ekleme
4 - Kitap Sil
5 - Baskı Yükseltme 
'q' - Çıkış 
""")

kutuphane = Kutuphane ()

while True :
    secim = str (input ("Yapmak istediğiniz işlemi seçiniz : "))

    if secim == 'q' :
        print ("Program sonlandırılıyor...")

        kutuphane.baglantiKesme ()
        sleep (2)

        print ("Program sonlandırıldı.")

        break

    elif secim == "1" :
        kutuphane.kitaplariGoster ()

    elif secim == "2" :
        isim = str (input ("Kitap ismi giriniz : "))
        print ("Kitap sorgulanıyor...")

        sleep (2)
        kutuphane.kitapSorgula (isim)

    elif secim == "3" :
        isim = str (input ("Kitap ismini giriniz : "))
        yazar = str (input ("Yazar ismini giriniz : "))
        yayinevi = str (input ("Yayınevini giriniz : "))
        tur = str (input ("Kitabın türünü giriniz : "))
        baski = int (input ("Baskı sayısını giriniz : "))

        kitap = Kitap (isim , yazar , yayinevi , tur , baski)

        print ("Kitap ekleniyor...")

        kutuphane.kitapEkle (kitap)
        sleep (2)

        print ("Kitap eklendi.")

    elif secim == "4" :
        isim = str (input ("Silmek istediğiniz kitabın ismini giriniz : "))

        cevap = str (input ("Emin misiniz (E / H) : "))

        if cevap == "E" :
            print ("Kitap siliniyor...")

            sleep (2)
            kutuphane.kitapSil (isim)

    elif secim == "5" :
        isim = str (input ("Kitabın ismini giriniz : "))

        print ("Baskı yükseltiliyor...")

        kutuphane.baskiYukselt (isim)
        sleep (2)

        print ("Baskı yükseltildi.")

    else :
        print ("Hatalı işlem seçtiniz.!")
        print ("Lütfen tekrar deneyiniz.")
