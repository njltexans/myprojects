# Magic methods are dunder methods (double underscore) __init__, __str__, __eq__
# __add__, __sub__, __mul__, __truediv__, __floordiv__, __mod__, __pow__, __and__, __or__, __xor__
#       - They are automatically called via python's built in operations
#       - They allow devs to define/customize behavior of objects


class book:

    def __init__(self, title, author, pages): # __init__ is a magic method
        self.title = title #defining attributes
        self.author = author
        self.pages = pages

    def __str__(self): # __str__ is a magic method
        return f"{self.title} by {self.author} is a fantastic book with {self.pages} pages."
    
    def __eq__(self, other): # __eq__ is a magic method, examining if two objects are equal
        return self.title == other.title and self.author == other.author # comparing two objects
    
    def __lt__(self, other): # __lt__ is a magic method, examining if one object is less than the other
        return self.pages < other.pages # comparing two objects
     
    def __getitem__(self, key): # __getitem__ is a magic method, allows for indexing
        if key == "title":
            return self.title
        if key == "author":
            return self.author
        if key == "pages":
            return self.pages
        return "Invalid key"
    

book1 = book("Magic of Python", "Noah.R.R Tolkien", 620)
book2 = book("Parry Hotter and The Smart Man's Stone", "N.L. Rowling", 320)
book3 = book("The House Cat, the Spookey Lady, and the Closet", "P.S. Newis", 420)


print(book1) # __str__ is called automatically
print(book2)
print(book3)

print(book1 == book2) # __eq__ is called automatically
print(book1 < book2) # __lt__ is called automatically

