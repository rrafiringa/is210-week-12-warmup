#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """
    Simple lookup function
    Args:
        var1 (mixed): An iterable type.
        var2 (int): Index
    Returns:
        dict: Dictionary of var1[var2] or empty
    """
    try:
        return var1[var2]
    except (IndexError, KeyError):
        print 'Warning: Your index/key does not exist'
        return var1

if __name__ == '__main__':
    print simple_lookup({}, 'banana')
