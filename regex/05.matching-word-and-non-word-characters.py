# https://www.hackerrank.com/challenges/matching-word-non-word/problem

Regex_Pattern = r"\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w"  # Do not delete 'r'.

# \w - word characters including a-z, A-Z, 0-9 and _
# \w - not word character

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())