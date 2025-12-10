#!/usr/bin/python3
"""CountedIterator tracks iteration count"""


class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        return self.count

    def __next__(self):
        self.count += 1
        return next(self.iterator)

    def __iter__(self):
        return self
