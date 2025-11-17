#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    control = False
    set_3 = set()

    for item in set_1:
        if item in set_2:
            control = False
        else:
            set_3.add(item)

    for item in set_2:
        if item in set_1:
            control = False
        else:
            set_3.add(item)

    return set_3
