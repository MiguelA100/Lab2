class Author:
    def __init__(self, name):
        self.name = name  # name of author
        self.books = []  # books published

    def publish (self, title):
        if title in self.books:
            print(f'Book \'{title}\' already exists!')
        else:
            self.books.append(title)

    def __str__(self):
        titles = ', '.join(self.books) or 'No published books'
        return f'Author: {self.name}, Books: {titles}'

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    school_id: str
    gpa: float

def main():

    Miguel = Student('Miguel', 347560, 3.5)
    Kate = Student('Kate', 12356, 2.0)

    print(Miguel)
    print(Kate)


