
# an interface could be created to define the methods that the iterator should have (__next__ and __iter__)
# however, since Python already has a built-in iterator protocol, this is not necessary
class BookIterator:
    def __init__(self, books):
        self.books = books
        self.index = 0

    def __next__(self):
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return book
        else:
            raise StopIteration

    def __iter__(self):
        return self