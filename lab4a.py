#!/usr/bin/env python3

def join_sets(s1, s2):
    """
    Returns a set containing all unique elements from both s1 and s2.
    This is the union of both sets.
    """
    return s1 | s2  # or s1.union(s2)

def match_sets(s1, s2):
    """
    Returns a set containing elements that are common to both s1 and s2.
    This is the intersection of the sets.
    """
    return s1 & s2  # or s1.intersection(s2)

def diff_sets(s1, s2):
    """
    Returns a set of elements that are in either s1 or s2, but not in both.
    This is the symmetric difference.
    """
    return s1 ^ s2  # or s1.symmetric_difference(s2)

if __name__ == '__main__':
    set1 = set(range(1,10))     # {1, 2, 3, 4, 5, 6, 7, 8, 9}
    set2 = set(range(5,15))     # {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
    print('set1: ', set1)
    print('set2: ', set2)
    print('join: ', join_sets(set1, set2))
    print('match: ', match_sets(set1, set2))
    print('diff: ', diff_sets(set1, set2))
