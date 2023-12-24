# https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        output = []
        for i in s:
            if i == "*":
                output.pop()
            else:
                output.append(i)
            
        return ''.join(output)
                
