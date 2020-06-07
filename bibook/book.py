from dataclasses import dataclass


@dataclass
class Book:
    '''
    A book.

    It contains basic data.
    '''

    author: str
    title: str
