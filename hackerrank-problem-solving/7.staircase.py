#!/bin/python3
# https://www.hackerrank.com/challenges/staircase/problem

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here

    for stair in range(1, n+1):
        stairs = "#" * stair
        print(stairs.rjust(n))

        # for stair in range(1, n+1):
        #     all_spaces = " " * (n-stair) 
        #     stairs = "#" * stair

        #     print(all_spaces + stairs)


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
