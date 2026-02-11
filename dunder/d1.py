class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def __str__(self):
        return f"'{self.title}' by {self.author} costs ₹{self.price}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', price={self.price})"

book1 = Book("Python Programming", "Guido van Rossum", 499)
book2 = Book("OOP Mastery", "James Gosling", 599)
print(book1)
print(book2)

print([book1, book2])
