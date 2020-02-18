import sqlite3
from time import sleep

class Kitap () :
    def __init__ (self , isim , yazar , yayinevi , tur , baski) :
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski

    def __str__ (self) :
        return "Kitap ismi : {}\nYazar : {}\nYayınevi : {}\nKitap Türü : {}\nBaskı : {}\n" .format (self.isim , self.yazar , self.yayinevi , self.tur , self.baski)

class Kutuphane () :
    def __init__ (self) :
        self.baglantiOlusturma ()

    def baglantiOlusturma (self) :
        self.con = sqlite3.connect ("kütüphane.db")
        self.cursor = self.con.cursor ()

        self.cursor.execute ("CREATE TABLE IF NOT EXISTS kitaplar (İsim TEXT , Yazar TEXT , Yayınevi TEXT , Tür TEXT , Baskı  INT)")

        self.con.commit ()

    def baglantiKesme (self) :
        self.con.close ()

    def kitaplariGoster (self) :
        self.cursor.execute ("SELECT * FROM kitaplar")
        data = self.cursor.fetchall ()

        if len (data) == 0 :
            print ("Kitap bulunmamaktadır.")

        else :
            for i in data :
                kitap = Kitap (i [0] , i [1] , i [2] , i [3] , i [4])

                print (kitap)

    def kitapSorgula (self , isim) :
        self.cursor.execute ("SELECT * FROM kitaplar WHERE İsim = ?" , (isim , ))
        data = self.cursor.fetchall ()

        if len (data) == 0 :
            print ("Böyle bir kitap bulunmamaktadır.")

        else :
            kitap = Kitap (data [0][0] , data [0][1] , data [0][2] , data [0][3] , data [0][4])

            print (kitap)

    def kitapEkle (self , ornek) :
        self.cursor.execute("INSERT INTO kitaplar VALUES (? , ? , ? , ? , ?)", (ornek.isim , ornek.yazar , ornek.yayinevi , ornek.tur , ornek.baski))
        self.con.commit ()


    def kitapSil (self , isim) :
        self.cursor.execute ("SELECT * FROM kitaplar WHERE İsim = ?" , (isim , ))
        data = self.cursor.fetchall ()

        if len (data) == 0 :
            print ("Böyle bir kitap bulunmamaktadır.")

        else :
            self.cursor.execute ("DELETE FROM kitaplar WHERE İsim = ?" , (isim , ))
            self.con.commit ()

            print ("Kitap silindi.")

    def baskiYukselt (self , isim) :
        self.cursor.execute ("SELECT * FROM kitaplar WHERE İsim = ?" , (isim , ))
        data = self.cursor.fetchall ()

        if len (data) == 0 :
            print ("Böyle bir kitap bulunmamaktadır.")

        else :
            baski = data [0][4]
            baski += 1

            self.cursor.execute ("UPDATE kitaplar SET Baskı = ? WHERE İsim = ?" , (baski , isim))
            self.con.commit ()