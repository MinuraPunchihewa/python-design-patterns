from book_library import BookLibrary


if __name__ == "__main__":
    library = BookLibrary()
    library.add_book("The Catcher in the Rye", "J. D. Salinger")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("1984", "George Orwell")

    for title, author in library.create_iterator():
        print(f"{title} by {author}")