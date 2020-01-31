# -*- coding: utf-8 -*-
from Book import Book
#First Book is file & second is Class

class Catalog:
    def __init__(self):
        self.different_book_count = 0
        self.books = []

    #As of now we are not implementing this @admin/librarian restrictions  
    #Only available to admin
    def addBook(self,name,author,publish_date,pages):
        b = Book(name,author,publish_date,pages)
        self.different_book_count += 1
        self.books.append(b)
        return b
    
    def removeBook(self,name,author,publish_date,pages):
        b = Book(name,author,publish_date,pages)
        for book in self.books:
            if book==b:
                self.books.remove(b)
                self.different_book_count -= 1
        return b

    #Only available to admin
    def addBookItem(self,book,isbn,rack):
        book.addBookItem(isbn, rack)
        
    def searchByName(self,name):
        for book in self.books:
            if name.strip() == book.name:
                return book

    # this method will retun book item details like isbn and rack because when a member issues a book we need this details. So, that when a member return it we can put it at the same place
    def bookDetails(self,name):
        for book in self.books:
            if name == book.name:
                bookDetail = [book.name, book.author, book.publish_date, book.pages]
                return bookDetail

    def searchByAuthor(self,author):
        for book in self.books:
            if author.strip() == book.author:
                return book
        
    def displayAllBooks(self):
        print ('Different Book Count',self.different_book_count)
        c = 0
        for book in self.books:
            c += book.total_count
            book.printBook()
        print ('Total Book Count',c)
           
    def removeBookItem(self,name,isbn):
        book = self.searchByName(name)
        book_item = book.searchBookItem(isbn)
        book.removeBookItem(book_item)


