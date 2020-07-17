"""Utilities for manipulating lists."""


def head(months):
    """Return the first item of the input list."""
    return months[0]
print(head(['Jan', 'Feb', 'Mar'])) # 'Jan'


def tail(months):
    """Return a new list of all items, excluding the first item."""

    return months[1:]
print(tail(['Jan', 'Feb', 'Mar'])) #['Feb', 'Mar']


def last(months):
    """Return the last item of the input list."""
    return months[2]
print(last(['Jan', 'Feb', 'Mar'])) #'Mar'


def top(months):
    """Return all elements of the input list except the last."""

    return months[:2]
print(top(['Jan', 'Feb', 'Mar'])) # ['Jan', 'Feb']

def first_three(months):
    """Return the first three elements of the input list."""

    return months[:3]
print(first_three(['Jan', 'Feb', 'Mar', 'Apr', 'May'])) #  ['Jan', 'Feb', 'Mar']


def last_five(numbers):
    """Return the last five elements of the input list."""

    return numbers[5:]
print(last_five([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])) # [15, 18, 21, 24, 27]


def middle(numbers):
    """Return all elements of input_list except the first two and the last two."""

    return numbers[2:8]
print(middle([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])) #[6, 9, 12, 15, 18, 21]



def inner_four(numbers):
    """Return the third, fourth, fifth, and sixth elements of input_list."""

    return numbers[2:6]
print(inner_four([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])) #[6, 9, 12, 15]


def inner_four_end(numbers):
    """Return the elements that are 6th, 5th, 4th, and 3rd from the end of input_list.

    This function should return those elements in a list, in the exact order
    described above."""

    return numbers[-6:-2]
print(inner_four_end([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])) #[12, 15, 18, 21]

def replace_head(numbers):
    """Replace the head of input_list with the value 42 and return nothing.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_head(multiples)
    >>> multiples == [42, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    True

    """
    numbers[0] = 42

    pass


def replace_third_and_last(numbers):
    """Replace third and last elements of input_list with 37 and return nothing.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_third_and_last(multiples)
    >>> multiples == [0, 3, 37, 9, 12, 15, 18, 21, 24, 37]
    True

    """
    numbers[2]  = 37
    numbers[-1] = 37
    pass


def replace_middle(numbers):
    """Replace all elements of a list but the first two and last two with 42 and 37.

    After the replacement, 42 and 37 should appear in that order in input_list.

    Return nothing.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_middle(multiples)
    >>> multiples == [0, 3, 42, 37, 24, 27]
    True

    """
    
    del numbers[4:8]
   
    numbers[2] = 42
    numbers[3] = 37
    pass


def delete_third_and_seventh(notes):
    """Remove third and seventh elements of input_list and return nothing.

    For example:

    >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
    >>> delete_third_and_seventh(notes)
    >>> notes == ['Do', 'Re', 'Fa', 'So', 'La', 'Do']
    True

    """
    notes.remove('Mi')
    notes.remove('Ti')

    pass


def delete_middle(notes):
    """Remove all elements from input_list except the first two and last two.

    Return nothing.

    For example:

    >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
    >>> delete_middle(notes)
    >>> notes == ['Do', 'Re', 'Ti', 'Do']
    True

    """
    del notes[2:6]

    pass


# This is the part were we actually run the doctests.

if __name__ == '__main__':
    import doctest

    result = doctest.testmod()
    if result.failed == 0:
        print('ALL TESTS PASSED')
