#!/usr/bin/python3
from functools import reduce

def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_values_weights = reduce(lambda acc, item: acc + (item[0] * item[1]), my_list, 0)
    sum_weights = reduce(lambda acc, item: acc + item[1], my_list, 0)
    return sum_values_weights / sum_weights
