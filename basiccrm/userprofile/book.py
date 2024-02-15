class Author:
    def __init__(self, author_id, name):
        self.author_id = author_id
        self.name = name

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []
        self.authors = []

    def add_author(self, author_id, name):
        author = Author(author_id, name)
        self.authors.append(author)
        print(f"Author '{name}' added successfully.")

    def add_book(self, book_id, title, author_id):
        author = next((a for a in self.authors if a.author_id == author_id), None)
        if author:
            book = Book(book_id, title, author)
            self.books.append(book)
            print(f"Book '{title}' added successfully.")
        else:
            print(f"Author with ID {author_id} not found.")

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]
        print(f"Book '{title}' removed successfully.")

if __name__ == "__main__":
     library = Library()

     while True:
        print("\nLibrary Management System Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("q. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author_id = input("Enter Author ID: ")
            library.add_book(book_id, title, author_id)
        elif choice == '2':
            title = input("Enter the title of the book to remove: ")
            library.remove_book(title)
        elif choice.lower() == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
