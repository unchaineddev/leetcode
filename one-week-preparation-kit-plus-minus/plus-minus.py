# https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem

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
    pos, neg, zer = 0, 0, 0
    for val in arr:
        if val < 0:
            neg += 1
        elif val > 0:
            pos += 1
        else:
            zer += 1
    
    pos1 = round(pos/n, 6)
    neg1 = round(neg/n, 6)
    zer1 = round(zer/n, 6)
    print(f'{pos1}\n{neg1}\n{zer1}')
            
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
