from PySide2.QtWidgets import QListWidgetItem, QWidget

from bibook.ui.ApplicationWidget_ListWidget import Ui_ApplicationWidget


class ApplicationWidget(QWidget):
    '''
    Main widget.

    It displays a list of books, and actions users can do.
    '''

    def __init__(self, parent=None):
        super(ApplicationWidget, self).__init__(parent=parent)

        self.__books = None
        self.__borrowed_books = []

        self.__ui = Ui_ApplicationWidget()
        self.__ui.setupUi(self)

        self.__ui.borrowBookButton.clicked.connect(self.__borrow_book)

    def set_books(self, books):
        self.__books = books
        for book in books:
            QListWidgetItem(
                book.title + ", by " + book.author,
                self.__ui.bookListWidget,
            )

    def __borrow_book(self):
        row = self.__ui.bookListWidget.currentRow()
        if row >= 0:
            book = self.__books[row]

            self.__borrowed_books.append(book)

            self.__ui.statusLabel.setText(
                u"Book \"%s\" borrowed!" % book.title)
