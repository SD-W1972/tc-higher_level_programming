#!/usr/bin/python3
"""VerboseList class extending Python list with notifications"""


class VerboseList(list):
    """List that prints notifications for modifications"""

    def append(self, item):
        """Add item to list with notification"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list with items from iterable with notification"""
        items_added = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{items_added}] items.")

    def remove(self, item):
        """Remove item from list with notification"""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop item from list with notification"""
        item = self[index] if self else None
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
