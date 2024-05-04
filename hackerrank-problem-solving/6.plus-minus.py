# https://www.hackerrank.com/challenges/plus-minus/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos, neg, zero = 0, 0, 0
    total = len(arr)

    for ele in arr:
        if ele > 0:
            pos += 1
        elif ele==0:
            zero += 1
        else:
            neg += 1

    positive = pos/total
    negative = neg/total
    zero_num = zero/total

    print(f'{positive: .6f}\n{negative: .6f}\n{zero_num: .6f}')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
