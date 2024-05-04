# https://www.hackerrank.com/challenges/matching-x-repetitions/problem

Regex_Pattern = r'^[A-Za-z24680]{40}[13579\s]{5}$'  # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
