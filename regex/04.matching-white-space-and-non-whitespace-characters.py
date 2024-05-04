# https://www.hackerrank.com/challenges/matching-whitespace-non-whitespace-character/problem

Regex_Pattern = r"\S\S\s\S\S\s\S\S"	# Do not delete 'r'.

# \s white-space, \S non-whitespace
# \s is any white-space [ \r\n\t\f ]
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())