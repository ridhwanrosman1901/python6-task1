class Book:
    total_books = 0
    
    def __init__(self, title, author):
        self.title = title
        self.author = author

        Book.total_books += 1

    def get_info(self):
        return f"{self.title} by {self.author}"

    @classmethod
    def get_total_books(cls):
        return cls.total_books
    
    @staticmethod
    def is_valid_title(title):
        return isinstance(title, str) and bool(title)

book_1 = Book("The Lessons of Demonic Magic", "Lucifer Jeremy White")
book_2 = Book("The Laws of The Great Architect", "Robin Sacredfire")

print(book_1.get_info())
print(book_2.get_info())

print(Book.is_valid_title("Demonic"))
print(Book.get_total_books())
