# Aggregation represents a relationship where one object contains references to one or more other objects.
#   - One object is the owner and the other object is the owned.
#   - In other words, an object is dependent on another object.


class library: # the whole "container" class
    def __init__(self, name):
        self.name = name
        self.books = [] # the "contained" object

    def add_book(self, book): # passing in the "contained" objects
        self.books.append(book) # adding the "contained" objects to the "container" object

    def show_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")


class book: # the "contained" class
    def __init__(self, title, author):
        self.title = title
        self.author = author


library = library("Noah's Library of Happiness and Tolerance")

book1 = book("Noah is very cool", "Soah Nmith")
book2 = book("How Noah conquered the world", "Smithers Noahe")
book3 = book("Noah's guide to happiness", "Noahbob Smitherstein III") 

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(f"{library.name} highly recommends the following books:")
library.show_books()
# The library class is the container class, and the book class is the contained class.








