# Leetcode Problem #2395: Find Subarrays With Equal Sum

# Description: Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum. Note that the two subarrays must begin at different indices. Return true if these subarrays exist, and false otherwise. A subarray is a contiguous non-empty sequence of elements within an array.

class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        d = {}
        left, right, size = 0, 2, len(nums)
        while left < size - 1:
            x = sum(nums[left:right])
            if x in d:
                return True
            else:
                d[x] = ''
            left += 1
            right += 1
        return False

s = Solution()

nums = [4,2,4]
print(s.findSubarrays(nums))

nums = [1,2,3,4,5]
print(s.findSubarrays(nums))

nums = [0,0,0]
print(s.findSubarrays(nums))
