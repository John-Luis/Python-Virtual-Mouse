


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True  # Default state when a book is added

    def __str__(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"'{self.title}' by {self.author} [{status}]"


class Library:
    def __init__(self):
        self.books = []  # This list is our "database"

    def add_book(self, book_obj):
        self.books.append(book_obj)
        print(f"Added: {book_obj.title}")

    def show_all_books(self):
        print("\n--- Current Library Collection ---")
        for book in self.books:
            print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_available:
                    book.is_available = False
                    print(f"\nYou have successfully borrowed '{book.title}'.")
                    return
                else:
                    print(f"\nSorry, '{book.title}' is already checked out.")
                    return
        print(f"\nBook '{title}' not found in library.")

# --- Testing it out ---
my_library = Library()

# We create Book objects and "pass" them into the library
my_library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
my_library.add_book(Book("1984", "George Orwell"))

print(books.)