class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                print("Livres supprimmés : ", book.title)
                break

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrow_books.append(book)
                break

    def return_book(self, book_title):
        for book in self.borrow_books:
            if book.title == book_title:
                self.borrow_books.remove(book)
                self.books.append(book)
                print("Livres retournés : ", book.title)
                break

    def available_books(self):
        return [book.title for book in self.books]
    
    def borrowed_books(self):
        return [book.title for book in self.borrow_books]
    
# Exemple d'utilisation de chacune des méthodes de la classe Library
library = Library()
book1 = Book("Le crime de l'Orient Express", "Agatha Christie", 1934)
book2 = Book("Le signal", "Maxime Chattam", 2018)

# Ajout de 2 livres à la biblio
library.add_book(book1)
library.add_book(book2)
print("Livres disponibles après ajout :")
print(library.available_books())
# Emprunt

library.borrow_book("Le crime de l'Orient Express")
print("Livres empruntés :")
print(library.borrowed_books())
print("Livres disponibles après emprunt :")
print(library.available_books())

# Retour
library.return_book("Le crime de l'Orient Express")
print("Livres disponibles après retour :")
print(library.available_books())

# Suppression
library.remove_book("Le signal")
print("Livres disponibles après suppression :")
print(library.available_books())
