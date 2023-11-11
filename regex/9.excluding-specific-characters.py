# https://www.hackerrank.com/challenges/excluding-specific-characters/problem

Regex_Pattern = r'^[^0-9][^aeiou][^bcDF][^\s][^AEIOU][^.,]$'	# Do not delete 'r'.


# String must be of length 6.
# First character should not be a digit (  or  ).
# Second character should not be a lowercase vowel (  or  ).
# Third character should not be b, c, D or F.
# Fourth character should not be a whitespace character ( \r, \n, \t, \f or <space> ).
# Fifth character should not be a uppercase vowel (  or  ).
# Sixth character should not be a . or , symbol.


import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())