#!/usr/bin/python3
"""Search and update module"""


def append_after(self, filename="", search_string ="", new_string=""):
    """append after function"""
    lines = []

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w') as f:
        f.writelines(lines)
