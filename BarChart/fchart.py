"""Take an input string and produce a bar chart.

Bar chart is produced by printing each letter
dictionary style, followed by showing the amount
of times each letter appeared.
Example: {'a': ['a','a','a','a','a']}
"""

import pprint
from translate_text import translate

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def print_chart(string):
    """Split a string into letters, then 'chart' it."""
    bar_dict = {key:[] for key in ALPHABET}
    for char in string:
        char = char.lower()
        if char in ALPHABET:
            bar_dict[char].append(char)
    pprint.pprint(bar_dict, width=110)

def compare_charts():
    """Take input in English, translate, and output as 2 charts."""
    print("You may need to stretch the console window if text wrapping occurs.")
    input_text = input("Please input text to be charted:\n")
    translation = translate(input_text)
    print("Translation:\n"+translation)
    print("English chart:")
    print_chart(input_text)
    print("Spanish chart:")
    print_chart(translation)

if __name__ == "__main__":
    compare_charts()
