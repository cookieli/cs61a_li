def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    "*** YOUR CODE HERE ***"
    start_a = a
    start_b = b
    c = a % b
    while c != 0:
        a = b
        b = c
        c = a % b
    return (start_a * start_b) // b
def has_digit(n, k):
    s = list(map(int,str(n)))
    for elem in s:
        if elem == k:
            return True
    return False

def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    count = 0
    for elem in range(10):
        if has_digit(n, elem):
            count = count + 1
    return count