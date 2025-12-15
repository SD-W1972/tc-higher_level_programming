#!/usr/bin/python3
"""Search and update module"""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after lines containing search_string"""
    lines = []

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)
