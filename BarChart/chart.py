"""Take an input string and produce a bar chart.

Bar chart is produced by printing each letter
dictionary style, followed by showing the amount
of times each letter appeared.
Example: {'a': ['a','a','a','a','a']}
"""

import pprint
from collections import defaultdict

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def print_chart(string):
    """Split a string into letters, then 'chart' it."""
    bar_dict = defaultdict(list)
    for char in string:
        char = char.lower()
        if char in ALPHABET:
            bar_dict[char].append(char)
    pprint.pprint(bar_dict, width=110)

if __name__ == "__main__":
    print("You may need to stretch the console window if text wrapping occurs.")
    print_chart(input("Please input text to be charted:\n"))
