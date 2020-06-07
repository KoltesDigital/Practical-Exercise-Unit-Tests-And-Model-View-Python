from bibook.book import Book


def test_book_creation():
    book = Book(
        author=u"Douglas Adams",
        title=u"The Hitchhiker's Guide to the Galaxy"
    )

    assert book.author == u"Douglas Adams"
    assert book.title == u"The Hitchhiker's Guide to the Galaxy"
