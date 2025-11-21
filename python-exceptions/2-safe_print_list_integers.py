#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(0, x):
            if isinstance(my_list[i], int):
                count += 1
                print(my_list[i], end="")
    except IndexError:
        pass
    print()
    return count
