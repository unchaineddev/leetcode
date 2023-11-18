# https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.replace("   ", " ").strip().split(" ")
        a = list(reversed(a))
        a = ' '.join(a)
        return a
            