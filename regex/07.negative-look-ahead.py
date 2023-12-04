# https://www.hackerrank.com/challenges/negative-lookahead/problem

Regex_Pattern = r"(.)(?!\1)"  # Do not delete 'r'.

# The negative lookahead (?!) asserts regex_1 not to be immediately followed by regex_2.
# Lookahead is excluded from the match (do not consume matches of regex_2),
# but only assert whether a match is possible or not.

# (.) This part of the pattern matches any single character except for a newline character.
# \1 is a backreference to the first capturing group (.).

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))