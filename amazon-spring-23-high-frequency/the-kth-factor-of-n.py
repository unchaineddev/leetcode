# https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = [i for i in range(1, n+1) if n % i == 0]

        for i, j in enumerate(factors):
            if i + 1 == k:
                return j
        return -1
