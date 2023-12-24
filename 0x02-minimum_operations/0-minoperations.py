#!/usr/bin/python3
'''Minimum Operations python3 challenge'''


def minOperations(n):
    '''calculates the fewest number of
    operations needed to result in exactly n H
    characters in this file.
    Returns:
        Integer : if n is impossible to achieve, return 0
    '''
    pasted_chars = 1  # check how many chars in the file
    clipboard = 0  # check how many H's copied
    counter = 0  # operations counter

    while pasted_chars < n:
        # if  not copied anything yet
        if clipboard == 0:
            # copy all
            clipboard = pasted_chars
            # increment operations counter
            counter += 1

        # if nothing pasted yet
        if pasted_chars == 1:
            # then paste
            pasted_chars += clipboard
            # increment operations counter
            counter += 1
            # then continue to next loop
            continue

        remaining = n - pasted_chars  # remaining chars to Paste
        # check if impossible by checking if clipboard
        # has more than needed to reach the number desired
        # which also means num of chars in file is equal
        # or more than in the clipboard.
        # in both situations it's impossible to achieve n of chars
        if remaining < clipboard:
            return 0

        # if can't be devided
        if remaining % pasted_chars != 0:
            # then paste current clipboard
            pasted_chars += clipboard
            # increment operations counter
            counter += 1
        else:
            # copy all
            clipboard = pasted_chars
            # then paste
            pasted_chars += clipboard
            # increment operations counter
            counter += 2

    # if got the target result
    if pasted_chars == n:
        return counter
    else:
        return 0
