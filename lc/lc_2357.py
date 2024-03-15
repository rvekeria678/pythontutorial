# Leetcode Problem #2357: Make Array Zero by Subtracting Equal Amounts

# Description: You are given a non-negative integer array nums. In one operation, you must: Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums, Subtract x from every positive element in nums. Return the minimum number of operations to make every element in nums equal to 0.

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        return len(set(x for x in nums if x != 0))
    
s = Solution()

nums = [1,5,0,3,5]
print(s.minimumOperations(nums))

nums = [0]
print(s.minimumOperations(nums))
