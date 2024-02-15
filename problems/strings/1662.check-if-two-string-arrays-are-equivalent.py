# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1 = " ".join(word1).replace(" ", "")
        word2 = " ".join(word2).replace(" ", "")
        if word1 == word2:
            return True
        else:
            return False


# One-liner
return "".join(word1) == "".join(word2)