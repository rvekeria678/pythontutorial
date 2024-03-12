# Leetcode Problem #961: N-Repeated Element in Size 2N Array

# Description: You are given an integer array nums with the following properties: nums.length == 2 * n, nums contains n + 1 unique elements, Exactly one element of nums is repeated n times. Return the element that is repeated n times.

class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        h = {}
        for num in nums:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1
        for i in h:
            if h[i] == len(nums) / 2:
                return i 
        return -1


s = Solution()

nums = [1,2,3,3]
print(s.repeatedNTimes(nums))

nums = [2,1,2,5,3,2]
print(s.repeatedNTimes(nums))

nums = [5,1,5,2,5,3,5,4]
print(s.repeatedNTimes(nums))
