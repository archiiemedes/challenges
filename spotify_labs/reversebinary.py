import sys


def reverse_str(s):
    return s[::-1]


def reverse_dec(n):
    """ Returns an integer representing the reversed binary of the
    given number.
    :param n: (int) number to reverse
    """
    n_as_bin = "{0:b}".format(n)
    return int(reverse_str(n_as_bin), 2)


if __name__ == "__main__":
    # ProblemID: Reversebinary
    #assert reverse_bin(13) == 11
    #assert reverse_bin(47) == 61
    n = sys.stdin.readline()
    print reverse_dec(int(n))