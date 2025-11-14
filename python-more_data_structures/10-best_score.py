#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = 0
    biggest_key = None
    for key,value in a_dictionary.items:
        if value > biggest:
            biggest = a_dictionary.get(key)
            biggest_key = key
    return biggest_key
