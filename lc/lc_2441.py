# Leetcode Problem #2441: Largest Positive Integer That Exists With Its Negative

# Description: Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array. Return the positive integer k. If there is no such integer, return -1.

class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        mx, d = -1, {}
        for i in nums:
            if i in d:
                mx = max(abs(i), mx)
            else:
                d[-i] = ''
        return mx
    
s = Solution()

nums = [-1,2,-3,3]
print(s.findMaxK(nums))
nums = [-1,10,6,7,-7,1]
print(s.findMaxK(nums))

nums = [-10,8,6,7,-2,-3]
print(s.findMaxK(nums))
