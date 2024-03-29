# Leetcode Problem #561: Array Partition

# Description: Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums = sorted(nums)
        res = 0
        for i in range(len(nums)//2):
            res += nums[2*i]
        return res


s = Solution()

nums = [1,4,3,2]
print(s.arrayPairSum(nums))

nums = [6,2,6,5,1,2]
print(s.arrayPairSum(nums))
