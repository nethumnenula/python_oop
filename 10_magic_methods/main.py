# Magic Methods = Dunder methods __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations
#                 They allow developers to define or customize the behavior of objects



from book import *


book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

print(book1)
print(book1 == book2)
print(book1 < book3)
print(book3+book1)

print("Lion" in book3)

print(book1['nm_pages'])