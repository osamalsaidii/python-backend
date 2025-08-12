class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} ({status})"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' added to the library.")

    def show_available_books(self):
        print(f"\nAvailable books in {self.name}:")
        available = [book for book in self.books if not book.is_borrowed]
        if not available:
            print("No books available.")
        else:
            for book in available:
                print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                print(f"You have borrowed '{title}'.")
                return
        print(f"Sorry, '{title}' is not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                print(f"You have returned '{title}'.")
                return
        print(f"No record of '{title}' being borrowed.")


if __name__ == "__main__":
    library = Library("City Library")

    library.add_book("1984", "George Orwell")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")

    library.show_available_books()
    library.borrow_book("1984")
    library.show_available_books()
    library.return_book("1984")
    library.show_available_books()
