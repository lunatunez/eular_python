"""Eular problem 2 - Even Fibonacci numbers:
    By considering the terms in the Fibonacci sequence whose values do not
    exceed 4 million, find the sum of the even-valued terms.
"""
import timer
DESC = 'Even Fibonacci numbers'
SOLUTION = 4613732


def fibonaccis(limit=None):
    """ Fibonacci number generator. Sequence starts [1, 1, 2, 3, 5] and so on. """
    a, b = 0, 1
    while True:
        if limit and b >= limit:
            raise StopIteration()
        a, b = b, a + b
        yield a


@timer.timeit
def solve():
    UPPERLIMIT = 4000000
    return sum([x for x in fibonaccis(UPPERLIMIT) if x % 2 == 0])
