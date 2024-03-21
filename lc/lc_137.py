# Leetcode Problem #137: Single Number II

# Description: Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it. You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        for num in d:
            if d[num] == 1:
                return num
        return -1

s = Solution()

nums = [2,2,3,2]
print(s.singleNumber(nums))

nums = [0,1,0,1,0,1,99]
print(s.singleNumber(nums))

nums = [30000,500,100,30000,100,30000,100]
print(s.singleNumber(nums))

