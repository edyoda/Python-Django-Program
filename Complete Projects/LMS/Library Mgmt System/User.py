# -*- coding: utf-8 -*
from Catalog import Catalog
from Book import Book

# Super Class
class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        
# Sub Class
class Member(User):
    def __init__(self, name, location, age, aadhar_id, student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.issuedBookItem = {}
        
    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id
    
    #assume name is unique
    def issueBook(self,catalog,book,name,days=10):
        issuedBookItemDetail = book.searchBookItemIsbn(book)
        self.issuedBookItem[self.student_id]=(issuedBookItemDetail)
        isbn=issuedBookItemDetail[0]
        catalog.removeBookItem(name,isbn)
    
    #assume name is unique
    def returnBook(self,catalog,book,name):
        isbn=self.issuedBookItem[self.student_id][1][0]
        rack=self.issuedBookItem[self.student_id][1][1]
        book.addBookItem(isbn,rack)
        
# Sub Class   
class Librarian(User):
    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        
    def __repr__(self):
        return self.name + self.location + self.emp_id
    
    def addBook(self,catalog,name,author,publish_date,pages):
        b = catalog.addBook(name, author, publish_date, pages)
        return b
    
    def removeBook(self,catalog,name):
        Book = catalog.bookDetails(name)
        catalog.removeBook(Book[0],Book[1],Book[2],Book[3])

    def addBookItem(self,book,isbn,rack):
        book.addBookItem(isbn, rack)
    
    def removeBookItemFromCatalog(self,catalog,book,name,isbn):
        catalog.removeBookItem(name,isbn)
    
        