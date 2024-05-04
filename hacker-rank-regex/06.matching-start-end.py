# https://www.hackerrank.com/challenges/matching-start-end/problem

Regex_Pattern = r"^\d\w\w\w\w\.$"  # Do not delete 'r'.

# ^ - start of string
# $ end of string

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())