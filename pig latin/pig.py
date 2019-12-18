"""A program that takes input and outputs it as pig latin."""
import re

def pig():
    """Take input and convert it to Pig Latin.

    First we take an input sentence, split that into words,
    and filter for punctuation and apply pig latin rules
    (To form Pig Latin, you take an English word that begins
    with a consonant, move that consonant to the end, and then
    add “ay” to the end of the word. If the word begins with a
    vowel, you simply add “way” to the end of the word.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    punctuation = {'.', ',', '!', '?', ';'}

    while True:
        phrase = input("Enter sentence to change to pig Latin:\n")
        new_string = ""

        for word in re.findall(r"[\w']+|[.,!?;]", phrase.lower()):
            if word in punctuation:
                new_string += word
            elif word[0] in vowels:
                new_string += (" "+word+"way")
            else:
                word_len = len(word)
                for i in range(word_len):
                    if word[i] in vowels:
                        new_string += (" "+word[i:]+word[:i]+"ay")
                        break
                else:
                    new_string += (" "+word+"ay")

        print(new_string.lstrip())

        try_again = input("\n\nTry again? (Press Enter or 'n' to quit)\n")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")

if __name__ == "__main__":
    pig()
