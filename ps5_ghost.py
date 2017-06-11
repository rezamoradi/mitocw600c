# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.


def possible_word_list(segment, word_list):
    """
    Returns a list of possible word list starting with segment
    :param segment: str
    :param word_list: list of str
    :rtype: list of str
    """

    length = len(segment)
    return list(filter(lambda x: x[:length] == segment, word_list))


def play_ghost():
    """
    play ghost game
    """
    current_word_fragment = ''
    counter = 0
    possible_wordlist = wordlist.copy()
    while True:
        print('Current word fragment: ', current_word_fragment)
        print("Player %d's turn." % (counter % 2 + 1))
        new_letter = input("Player %d's says letter: " % (counter % 2 + 1))

        if new_letter not in string.ascii_letters:
            continue

        current_word_fragment += new_letter.lower()
        possible_wordlist = possible_word_list(current_word_fragment, possible_wordlist)

        if len(possible_wordlist) == 0:
            print("Player %d loses because no word begins with %s." % (counter % 2 + 1, current_word_fragment))
            print("Player %d wins." % ((counter + 1) % 2 + 1))
            break

        if len(current_word_fragment) > 3 and current_word_fragment in possible_wordlist:
            print("Player %d loses because %s is a word." % (counter % 2 + 1, current_word_fragment))
            print("Player %d wins." % ((counter + 1) % 2 + 1))
            break

        counter += 1


if __name__ == '__main__':
    wordlist = load_words()
    play_ghost()