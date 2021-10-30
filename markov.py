"""Generate Markov text from text files."""

from random import choice
import string
from sys import argv


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_string = open(file_path).read()

    return text_string

# print(open_and_read_file("green-eggs.txt"))

def make_chains(text_string, n = 2):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    

    words = text_string.split()

    chains = {}
    chain_list = []

    for idx in range(len(words)-1):
        # loop n times
        # in the loop, add word[idx + n] to chain as a list then change to tuple
        # this creates a tuple of n words
        for i in range(n):
            try:
                chain_list.append(words[idx + i])
            except:
                pass
        chain = tuple(chain_list)
            # chain = (words[idx], words[idx+1])
        if chain not in chains: # if the chain does not already exist in the chains dictionary
            try: 
                chains[chain] = [words[idx + n]] # add values for that chain (single word that follows the chain)
            except:
                pass
        else:
            try:
                chains[chain].append(words[idx + n]) # if chain is already in dictionary, append the single word that follows chain to values
            except:
                pass
        chain_list = []

    return chains

# text_string = open_and_read_file("green-eggs.txt")
# print(make_chains(text_string, 4))


# Would you could you in a house?
# Would you could you with a mouse?
# Would you could you in a box?
# Would you could you with a fox?
# Would you like green eggs and ham?
# Would you like them, Sam I am?

def make_text(chains):
    """Return text from chains."""

    words = []

    first_choice_list = []

    for chain in chains.keys(): # check all the keys for capital first letter and add to first choice list
        if chain[0][0] in string.ascii_uppercase:
            first_choice_list.append(chain)

    chain = choice(first_choice_list) # first chain will be a random choice from first choice list
    words.append(' '.join(list(chain)))
    

    while chain in chains: # while the current chain is in the dictionary
        next_word = choice(list(chains[chain])) # next word is a random choice of the current chain's values
        chain = list(chain[1:])
        chain.append(next_word) # change chain to previous chain, excluding first word and add next word
        chain = tuple(chain)
        words.append(next_word)

    return ' '.join(words)


file_path = argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(file_path)

# Get a Markov chain
chains = make_chains(input_text, 3)
# print(chains)

# Produce random text
random_text = make_text(chains)

print(random_text)
