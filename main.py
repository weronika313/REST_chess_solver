# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

from models import Rook


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    king = Rook("H2")
    # Create a list in a range of 10-2

    # Print the list
    print(king.list_available_moves())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
