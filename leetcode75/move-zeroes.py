# https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_list = []
        other = []
        for n in nums:
            if n == 0:
                new_list.append(n)
            else:
                other.append(n)
        nums[:] = other + new_list


        