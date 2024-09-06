class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages 
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, other):
        return other in self.title or other in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            raise KeyError(f"Key {key} not found")
    
# Example usage:
book1 = Book("Harry Potter", "J.K. Rowling", 900)
book2 = Book("Lightning Thief", "Rick Riordan", 800)

print(book1)  # Uses __str__
print(book1 == book2)  # Uses __eq__
print(book1 < book2)  # Uses __lt__
print(book1 > book2)  # Uses __gt__
print(book1 + book2)  # Uses __add__
print("Potter" in book1)  # Uses __contains__
print(book1['title'])  # Uses __getitem__
print(book1['author'])  # Uses __getitem__
# print(book1['wow'])  # Uses __getitem__


print(book1.author)