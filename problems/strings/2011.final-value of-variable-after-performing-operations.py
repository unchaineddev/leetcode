# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # X = 0
        # for val in operations:
        #     if '++' in val:
        #         X += 1
        #     else:
        #         X -= 1
        # return X
        
        return sum(1 if '++' in val else -1 for val in operations)

        