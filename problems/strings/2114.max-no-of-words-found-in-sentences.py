# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_word = []
        for words in sentences:
            words = len(words.split(" "))
            max_word.append(words)
            
        return max(max_word)