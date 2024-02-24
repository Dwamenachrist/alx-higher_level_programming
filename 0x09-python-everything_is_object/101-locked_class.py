#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Make sure users can only create a new attribute in the LockedClass if it's named 'first_name'.
    """

    __slots__ = ["first_name"]