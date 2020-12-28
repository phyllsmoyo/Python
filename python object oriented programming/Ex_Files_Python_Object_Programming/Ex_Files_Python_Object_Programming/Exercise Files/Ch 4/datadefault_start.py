# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass, field
import random


def price_func():
    return float(random.randrange(20, 40))


@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No Title"
    author: str = "No Autor"
    pages: int = 0
    price: float = field(default_factory=price_func)


b1 = Book("Umzilakawulandelwa", "NS Sigogo", 235)
b2 = Book("Umzilaka", "NS ", 300)
print(b1)
print(b2)