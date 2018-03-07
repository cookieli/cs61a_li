HW_SOURCE_FILE = 'hw04.py'
from math import *
def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n -3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        first_before = 3
        second_before = 2
        third_before  = 1
        i = 4
        while i <= n:
            value = first_before + 2 * second_before + 3 * third_before
            third_before = second_before
            second_before = first_before
            first_before  = value
            i += 1
        return value

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def pingpong_num(k, p, up):
        if k == n:
            return p
        if up :
            return pingpong_switch(k+1, p+1, up)
        else:
            return pingpong_switch(k+1, p-1, up)
    def pingpong_switch(k, p, up):
        if has_seven(k) or k % 7 == 0:
            return pingpong_num(k, p, not up)
        else:
            return pingpong_num(k, p, up)
    return pingpong_switch(1, 1, True)

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    i = 0
    while 2**i <= amount:
        i += 1
    return count_partitions(amount, 2**(i - 1))
def count_partitions(n, m):
    if n == 0:# or n == 0:
        return 1
    elif n < 0:
        return 0
    elif m < 1:
        return 0
    else:
    #    print("n-m ",n-m, " m ",m)
    #    print("n ", n, " m: ",2**(int)(log2(m)-1))
    #    print(" ")
        return count_partitions(n-m, m) + count_partitions(n, 2**(int)(log2(m)-1))
###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'
