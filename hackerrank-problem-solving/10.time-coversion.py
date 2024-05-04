# https://www.hackerrank.com/challenges/time-conversion/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    hour_hand = int(s.split(":")[0])
    minute_sec_hand = s[2:8]
    am_or_pm = s[-2:].lower()

    if am_or_pm == 'am':
        if hour_hand < 12:
            return (s[0:8])
        elif hour_hand == 12:
            hour_hand = 0
            return f'{hour_hand:02d}{minute_sec_hand}'

    if am_or_pm == 'pm':
        if hour_hand < 12:
            hour_hand += 12
            return f'{hour_hand:02d}{minute_sec_hand}'
        else:
            return s[0:8]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
