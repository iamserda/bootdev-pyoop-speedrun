# Classes Practice
# Wizards are having a hard time keeping track of all the books in their library. They need your help to create a library system that will allow them to add, remove, and search for books.

# Magical incantations to find books have unfortunately not been invented yet.

# Assignment
# You've been tasked with writing the code for the wizard library. Complete the Library and Book classes listed below.

# Create the Book Class:
# Create the __init__(self, title, author) method
# Set .title and .author to the values of the parameters.
# Create the Library Class:
# Create the __init__(self, name) method
# Initialize a .name member variable to the value of the name parameter.
# Create a .books member initialized to an empty list.
# Add the add_book(self, book) method:
# Add book, the given Book instance, to the library's books instance variable by appending it to the end of the list.
# Add the remove_book(self, book) method:
# Create a new, empty list to hold the books you want to keep.
# Loop through every book in the library’s books list.
# If the book’s title or author do not match the one you want to remove, add it to the new list.
# After checking all the books, replace the library’s books list with the new list.
# Add the search_books(self, search_string) method:
# For every book in the library check if the search_string is contained in the title or author field (case-insensitive).
# Return a list of all books that match the search string, ordered in the same order as they were added to the library.
class Book:
    def __init__(self, title:str, author:str):
        self.title: str = title
        self.author: str = author
    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def __str__(self):
        message = f"Library: {self.name}\n==========================="
        for index, book in enumerate(self.books):
            message += f"\n{index + 1}. {book}"
        return message + "\n==========================="

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        new_books = []
        for b in self.books:
            if book.title == b.title:
                continue
            else:
                new_books.append(b)
        self.books = new_books

    def search_books(self, search_string:str):
        found_books = []
        for book in self.books:
            if search_string.lower() in book.title.lower() or search_string in book.author.lower():
                found_books.append(book)
        return found_books
    
    
the_lib = Library("Testing Library") 
the_lib.add_book(Book("The Trial", "Franz Kafka"))
the_lib.add_book(Book("The Catcher in the Rye", "J.D. Salinger"))
the_lib.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
the_lib.add_book(Book("1984", "George Orwell"))
print(the_lib)