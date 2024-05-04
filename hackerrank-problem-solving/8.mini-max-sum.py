#!/bin/python3
# https://www.hackerrank.com/challenges/mini-max-sum/problem

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    total_sum = sum(arr)
    min_sum = total_sum - max(arr)
    max_sum = total_sum - min(arr)
    print(f'{min_sum} {max_sum}')
    # final_list = []
    # for i in range(len(arr)):
    #     four_elements = random.sample(arr, 4)
    #     sum_of_four = sum(four_elements)
    #     final_list.append(sum_of_four)
    # print(f'{min(final_list)} {max(final_list)}')




if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)