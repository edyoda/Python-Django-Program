# -*- coding: utf-8 -*-
from Book import Book
from Catalog import Catalog
from User import Member, Librarian

# book object
b1 = Book('Shoe Dog','Phil Knight', '2015',312)
# adding book items
b1.addBookItem('123hg','H1B2')
b1.addBookItem('124hg','H1B3')

catalog = Catalog()

# book object
b = catalog.addBook('Shoe Dog','Phil Knight', '2015',312)
# adding book items
catalog.addBookItem(b, '123hg','H1B2')
catalog.addBookItem(b, '124hg','H1B4')
catalog.addBookItem(b, '125hg','H1B5')

b = catalog.addBook('Moonwalking with Einstien','J Foer', '2017',318)
catalog.addBookItem(b, '463hg','K1B2')

catalog.displayAllBooks()
# removing book item
catalog.removeBookItem('Shoe Dog','124hg')
catalog.displayAllBooks()

# serching a book
b = catalog.searchByName('Shoe Dog')
print(b)

#librarian object
librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101')
# librarian adding book
l = librarian.addBook(catalog, 'How to write clean code', 'David', '2020', 150)
l1 = Book('EdYoda python assignments solution', 'Awanti Das', '2020', 150)
# librarian adding book items
librarian.addBookItem(l, '1234hg', 'H1B2')
librarian.addBookItem(l, '1235hg', 'H1B2')
catalog.displayAllBooks()
# librarian removing bookitem we need to paas class object for calling class methods
librarian.removeBookItemFromCatalog(catalog,l1, 'EdYoda python assignments solution', '1234hg')
# librarian removing book
librarian.removeBook(catalog,'Shoe Dog')

# memeber Object
m1 = Member("Vish","Bangalore",23,'asljlkj22','std1233')
# member is issuing book and then system will update our inventory
m1.issueBook(catalog, b1, 'Shoe Dog')
catalog.displayAllBooks()

# when member returns a book,then system will update our inventory
m1.returnBook(catalog, b1, 'Shoe Dog')
catalog.displayAllBooks()