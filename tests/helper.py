#!/usr/bin/python3
"""Define helper functions"""


def remove_file(file: str) -> None:
    """Remove a file"""
    import os

    try:
        os.remove(file)
    except FileNotFoundError:
        pass
