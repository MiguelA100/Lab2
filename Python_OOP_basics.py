class author:
    def __init__(self, author, books_published):
        self.author = author
        self.books = books_published

    def __str__ (self):
        return f'author{self.author}, books: {self.books} published'

def publish(self, title):
    if title in self.books:
        print(f'Book \'{title}\' already exists!')

    else:
        self.books.append(title)

def main():
    class Student:
        name: str
        school_id: str
        gpa: float

