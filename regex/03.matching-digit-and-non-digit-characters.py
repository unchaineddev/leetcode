# https://www.hackerrank.com/challenges/matching-digits-non-digit-character/problem
Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"	# Do not delete 'r'.
# \d is digit, \D is not digit

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())