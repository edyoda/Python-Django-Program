# -*- coding: utf-8 -*-
from BookItem import BookItem

class Book:
    def __init__(self,name,author,publish_date,pages):
        self.name = name
        self.author = author
        self.publish_date = publish_date
        self.pages = pages
        self.total_count = 0
        self.book_item = []
        
    # adding a book item    
    def addBookItem(self,isbn,rack):
        b = BookItem(self,isbn,rack)
        self.book_item.append(b)
        self.total_count +=1
    
    # Displaying all Books
    def printBook(self):
        print (f'Book Name: {self.name}\nAuthor Name: {self.author}\nAvailable at:')
        for book_item in self.book_item:
            print (f'Rack: {book_item.rack}\tIsbn: {book_item.isbn}')
            
        # Search Books by name
    def searchBookItem(self,isbn):
        for book_item in self.book_item:
            if isbn.strip() == book_item.isbn:
                return book_item

    #it will return book's book_item like isbn and rack so that we can remove book and remove it from our inventory and revert the saem action when i member returns it 
    def searchBookItemIsbn(self,book):
        for book_item in self.book_item:
            if book == book_item.book:
                issuedBookItem = [book_item.isbn, book_item.rack]
                return issuedBookItem
            
    # Renove a specing Book Item
    def removeBookItem(self,book_item):
        if book_item in self.book_item:
            self.book_item.remove(book_item)
            self.total_count -=1
            
    def __repr__(self):
        return self.name + ' ' + self.author + ' ' + str(self.publish_date) + ' ' + str(self.pages)
