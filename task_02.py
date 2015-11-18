#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """
    User defined Exception subclass
    """
    pass


def get_age(birthyear):
    """
    Get the age
    Args:
        birthyear (int): Year
    Returns:
        int: Age
    """

    age = datetime.datetime.now().year - birthyear
    if age < 1:
        raise InvalidAgeError()
    return age


if __name__ == '__main__':
    print get_age(2087)
