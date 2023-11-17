# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out1 = ''.join(map(''.join, zip(word1, word2)))

        if len(word1) > len(word2):
            return (out1 + ''.join(word1[-2:]))
        elif len(word2) > len(word1):
            return (out1 + ''.join(word2[-2:]))
        else:
            return (out1)
