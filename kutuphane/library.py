import os
import time
import sqlite3 as sql

class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def __str__(self):
        return (username,pasword)

class Book():
    def __init__(self, name, author, type, pagenumber, status):
        self.name = name.lower()
        self.author = author.lower()
        self.type = type.lower()
        self.pagenumber = pagenumber
        self.status = status
    def __str__(self):
        if self.status == 0:
            return "Name: {}\nAuthor: {}\nType: {}\nPage Number: {}\n".format(self.name,self.author,self.type,self.pagenumber) + "This book in library."
        else:
            return "Name: {}\nAuthor: {}\nType: {}\nPage Number: {}\n".format(self.name,self.author,self.type,self.pagenumber) + "This book in reader."

class Library():
    def __init__(self):
        self.ConnectDatabase()
    
    def ConnectDatabase(self):
        self.con = sql.connect("library.db")
        self.im = self.con.cursor()
        self.im.execute("CREATE TABLE IF NOT EXISTS books (name TEXT, author TEXT, type TEXT, pagenumber INT, status INT)")
        self.con.commit()

    def ExitDatabase(self):
        self.con.close()

    def AddBook(self, example):
        self.im.execute("INSERT INTO books VALUES (?,?,?,?,?)",(example.name, example.author, example.type, example.pagenumber, example.status))
        self.con.commit()

    def ShowBooks(self):
        self.im.execute("SELECT * FROM books")
        values = self.im.fetchall()
        if values == []:
            print("Kütüphanede kitap bulunmamaktadır..\nEklemek için geri dönün")

        else:
            for i in values:
                book = Book(i[0], i[1], i[2], i[3], i[4])
                print(book)

    def SelectBook(self, name):
        name = name.lower()
        self.im.execute("SELECT * FROM books WHERE name = ?", (name, ))
        values = self.im.fetchall()
        
        if values == []:
            print("Aradığınız kitap bulunmamaktadır..\n Eklemek için geri gönün..")
            time.sleep(2)
            os.system("cls")
        else:
            print("Kitap kütüphanemizde bulunmaktadır.")
            time(2)
            os.system("cls")

    def LendBook(self,name):
        self.im.execute("SELECT * FROM books WHERE name=?", (name,))
        values = self.im.fetchall()
        
        if values == []:
            print("Aradığınız kitap bulunmamaktadır..\n Eklemek için geri gönün..")
        else:
            for i in values:
                book = Book(i[0], i[1], i[2], i[3], i[4])
                if book.status == 0:
                    self.im.execute("UPDATE books SET status=? WHERE name=?",(1,name))
                    print("Kitap başarıyla okuyucuya verildi.")
                    self.con.commit()
                    os.system("cls")
                else:
                    print("Vermek istediğiniz kitap şu an başka bir okuyucudadır.Lütfen daha sonra deneyin.")
                    os.system("cls")

    
    def TakeBook(self,name):
        self.im.execute("SELECT * FROM books WHERE name=?", (name,))
        values = self.im.fetchall()
        
        if values == []:
            print("Aradığınız kitap bulunmamaktadır..\n Eklemek için geri gönün..")
        else:
            for i in values:
                book = Book(i[0], i[1], i[2], i[3], i[4])
                if book.status == 1:
                    self.im.execute("UPDATE books SET status=? WHERE name=?",(0,name))
                    print("Kitap başarıyla geri alındı.")
                    self.con.commit()
                else:
                    print("Vermek istediğiniz kitap şu an kütüphanededir.Lütfen daha farklı bir kitap deneyin.")



class Login():
    def __init__(self):
        self.ConnectDatabase1()

    def ConnectDatabase1(self):
        self.con2 = sql.connect("users.db")
        self.cur = self.con2.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS users (username, password)")
        self.con2.commit()
    
    def ExitDatabase1(self):
        self.con2.close()

    def CreateUser(self, example):
        self.cur.execute("INSERT INTO users VALUES (?,?)",(example.username,example.password))
        self.con2.commit()

    def LoginCheck(self,user):
        self.cur.execute("SELECT * FROM users WHERE username=? AND password=?",(user.username, user.password))
        data = self.cur.fetchall()
        
        if data == []:
            print("Böyle bir kullanıcı yok. Tekrar deneyin..")
            time.sleep(1)
            return 0
        elif [(user.username, user.password)]:
            print(" Hoşgeldiniz..")
            time.sleep(1)
            return "*"
        else:
            print("Failed!.\nTry Again.")
            return 1
            
