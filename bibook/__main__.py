import sys

from PySide2.QtWidgets import QApplication

from bibook.application_widget import ApplicationWidget
from bibook.book import Book

app = QApplication(sys.argv)

main_window = ApplicationWidget()
main_window.set_books([
    Book(
        author=u"Gerald Weinberg",
        title=u"Quality Software Management",
    ),
    Book(
        author=u"Robert L. Glass",
        title=u"Building quality software",
    )
])
main_window.show()

code = app.exec_()

del main_window
sys.exit(code)
