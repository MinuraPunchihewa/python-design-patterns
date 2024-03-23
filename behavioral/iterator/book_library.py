from i_collection import ICollection
from book_iterator import BookIterator


class BookLibrary(ICollection):
    def __init__(self):
        self._books = []

    def add_book(self, title, author):
        self._books.append((title, author))

    def create_iterator(self):
        return BookIterator(self._books)