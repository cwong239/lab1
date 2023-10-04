# Lab 1
from typing import *

# Data Definition
# We will represent the temperature with its degree. Which is a float.

celsius: TypeAlias = int
fahrenheit: TypeAlias = float


def convert_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


celsius1 = 21
print(convert_to_fahrenheit(celsius1))

celsius2 = 28
print(convert_to_fahrenheit(celsius2))
# Data Definition
# We will represent the price in cents. It is an integer.
price: TypeAlias = int


# Data Definition
# We will represent the price record with its name and the price. The name is a string and the
# price is an integer.
class PriceRecord:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'PriceRecord{self.name, self.price}'

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price


pr1 = PriceRecord("h", 12)
print(pr1)

pr2 = PriceRecord("d", 35)
print(pr2)


# Data Definition
# We will represent the date with the day, month, and year, which are all integers.
class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        return f'Date{self.day, self.month, self.year}'

    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and self.year == other.year


# Data Definition
# We will represent the open tab with its url and the date.
class OpenTab:
    def __init__(self, url, date):
        self.url = url
        self.date = date

    def __repr__(self):
        return f'OpenTab{self.url, self.date}'

    def __eq__(self, other):
        return self.url == other.url and self.date == other.date


date1 = Date(4, 10, 2023)
url1 = "http://example.com"
print(OpenTab(url1, date1))

date2 = Date(30, 2, 2001)
url2 = "https://findtheinvisiblecow.com/"
print(OpenTab(url2, date2))


