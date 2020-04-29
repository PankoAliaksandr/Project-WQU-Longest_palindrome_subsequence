import numpy as np


# Solving function
def find_polindrom(sequence):
    n = len(sequence)

    # Create a table to store results of subproblems
    palindrome_lengths = np.zeros((n, n))

    # Strings of length 1 are palindrome of length 1
    np.fill_diagonal(palindrome_lengths, 1)

    for substr_length in range(2, n + 1):
        for i in range(n - substr_length + 1):
            j = i + substr_length - 1
            if sequence[i] == sequence[j] and substr_length == 2:
                palindrome_lengths[i][j] = 2
            elif sequence[i] == sequence[j]:
                palindrome_lengths[i][j] = palindrome_lengths[i + 1][j - 1] + 2
            else:
                palindrome_lengths[i][j] = max(palindrome_lengths[i][j - 1],
                                               palindrome_lengths[i + 1][j])
    palindrome_left = ''
    middle = ''
    n, n = np.shape(palindrome_lengths)
    # start in the north-eastern corner of the matrix
    substr_length, end = n - 1, n-1
    # traceback
    while substr_length > 0 and end > 1:
        start = end - substr_length
        # if possible, go left
        if palindrome_lengths[start][end] == (
                palindrome_lengths[start][end - 1]):
            substr_length -= 1
            end -= 1
        # the left cell == current - 2, but the lower is the same as current,
        # go down
        elif palindrome_lengths[start][end] == (
                palindrome_lengths[start + 1][end]):
            substr_length -= 1
        # both left and lower == current - 2, go south-west
        else:
            palindrome_left += sequence[start]
            substr_length -= 2
            end -= 1
    if palindrome_lengths[start][end] == 1 and substr_length >= 0:
        middle = sequence[start+1]
    result = ''.join(palindrome_left) + middle + ''.join(palindrome_left[::-1])
    return result


# "a man two cats a crazy plan aibohphobia and a canal in panama"
string = raw_input("Enter a string:")
print(find_polindrom(string))
