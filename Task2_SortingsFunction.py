"""
@author: Lingling Yao
@since: 27/04/2018
@modified: 01/05/2018
@functionality: This file contains two sorting functions.
"""


def insertion_sort_as(b_list):
    # tested
    n = len(b_list)
    for i in range(n):
        for j in range(i, 0, -1):
            if b_list[j] < b_list[j-1]:
                b_list[j], b_list[j-1] = b_list[j-1], b_list[j]


def insertion_sort_de(b_list):
    # tested
    n = len(b_list)
    for i in range(n):
        for j in range(i, 0, -1):
            if b_list[j] > b_list[j-1]:
                b_list[j], b_list[j-1] = b_list[j-1], b_list[j]
