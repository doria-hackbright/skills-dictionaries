"""Advanced skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""


def top_characters(input_string):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example:

        >>> top_characters("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:

        >>> top_characters("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    # strip all whitespace from input_string
    input_string = "".join(input_string.split())

    # start a new dictionary to keep track of characters and counts
    character_counts = {}

    # iterate through each character and gather up the dictionary counts
    for letter in input_string:
        character_counts[letter] = character_counts.get(letter, 0) + 1

    # create a sorted list of tuples based on the character_counts dictionary
    # it sorts in descending order based on the second item of each tuple
    sorted_dict = sorted(character_counts.items(),
                         key=lambda t: t[1],
                         reverse=True)

    # initiate an empty list to store the highest count characters
    # also set the default highest count to the first dictionary entry
    # since it is in descending order
    top_chars = []
    high_count = sorted_dict[0][1]

    # iterate through each item in the sorted_dict list and find high counts
    for item in sorted_dict:
        if item[1] >= high_count:
            top_chars.append(item[0])

    return top_chars


def adv_alpha_sort_by_word_length(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    word_lengths = {}

    # looked up setdefault() dictionary method in python documentation
    # binds a new default value to a key if the key does not yet exist

    for word in words:
        word_lengths.setdefault(len(word), []).append(word)

    # sort each list value for each key in the dictionary
    for key in word_lengths:
        word_lengths[key].sort()

    return sorted(word_lengths.items())

##############################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
