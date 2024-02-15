# https://leetcode.com/problems/truncate-sentence/

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # for i in s:
        #     values = s.split(" ")
        # return " ".join(values[:k])

        words = s.split(" ")
        return " ".join(words[:k])

        
