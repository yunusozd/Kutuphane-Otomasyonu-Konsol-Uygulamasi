import time
import os
from library import *

library = Library()
login = Login()
login_screen = """Library Management System
1.Login
2.Sign up
q.Exit
"""
library_opening = """Library Management System
1.Add Book Into Library
2.Show all books
3.Search for Books
4.Lend Book
5.Take book
q.Exit
"""
def main():
    question = input(library_opening+"Choose one\n ->")
    if question == "1":
        book_name = input("What is name of the book?\n ->")
        book_author = input("Who wrote this book?\n ->")
        book_type = input("What is the type of book?\n ->")
        page_number = int(input("How many page in the book?\n ->"))
        status = 0
        book = Book(book_name,book_author,book_type,page_number,status)
        library.AddBook(book)
        print("Successfully added.")
    elif question == "2":
        print("All books in our Library:")
        library.ShowBooks()
    elif question == "3":
        key2 = input("What is the name of the book you looking for?\n ->")
        library.SelectBook(key2)
    elif question == "4":
        key3 = input("Which book do you lend for? (Enter the name of the book.)\n ->")
        time.sleep(2)
        library.LendBook(key3)
        time.sleep(1)
    elif question == "5":
        key4 = input("Which book do you take back for? (Enter the name of the book.)\n ->")
        library.TakeBook(key4)
    elif question == "q":
        print("log Out..\nGood BYE.")
        time.sleep(2)
        os.system("exit")
    else:
        print("You typed wrong number.Please try again.")
        time.sleep(1)
        
while True:
    key = input(login_screen+"Please choose one. \n ->")
    os.system("cls")
    if key == "q":
        print("Log out")
        time.sleep(2)
        break
    elif key == "1":
        print("*************************")
        username1 = input("Username: ")
        password1 = input("Password: ")
        user = User(username1,password1)
        login.LoginCheck(user)
        if login.LoginCheck(user) == 0 and 1:
            break
        elif login.LoginCheck(user) == "*":
            os.system("cls")
            main()
        
    elif key == "2":
        print("Insert username and password.")
        username2 = input("Username: ")
        password2 = input("Password: ")
        user2 = User(username2,password2)
        login.CreateUser(user2)
        print("Successfully sign on")
        print("Redirecting to the main page.Please wait.")
        time.sleep(1)
        os.system("cls")
    else:
        print("You typed wrong number.Please try again.")
        time.sleep(1)
        os.system("cls")
