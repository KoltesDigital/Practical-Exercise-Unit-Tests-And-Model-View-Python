from PySide2.QtCore import QAbstractListModel, QModelIndex, Qt, Slot


class BookListModel(QAbstractListModel):
    '''
    A model showing a list of books.
    '''

    def __init__(self, parent=None):
        super(BookListModel, self).__init__(parent=parent)

        self.__books = None

    def books(self):
        return self.__books

    @Slot(list)
    def set_books(self, books):
        self.beginResetModel()
        self.__books = books
        self.endResetModel()

    @staticmethod
    def _get_data(_row, book, role):
        if role in (Qt.DisplayRole, Qt.EditRole):
            return book.title + ", by " + book.author

        if role == Qt.UserRole:
            return book

        return None

    def data(self, index, role):
        if not index.isValid():
            return None

        row = index.row()
        if row < 0 or row >= self.rowCount():
            return None

        book = self.__books[row]
        return self._get_data(row, book, role)

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0

        if self.__books is None:
            return 0

        return len(self.__books)
