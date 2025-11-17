#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_values_weights = 0
    sum_weights = 0

    for score, weight in my_list:
        sum_values_weights += score * weight
        sum_weights += weight

    return sum_values_weights / sum_weights
