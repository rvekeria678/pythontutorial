# Leetcode Problem #2945: Find Maximum Non-decreasing Array Length

# Description: You are given a 0-indexed integer array nums. You can perform any number of operations, where each operation involves selecting a subarray of the array and replacing it with the sum of its elements. For example, if the given array is [1,3,5,6] and you select subarray [3,5] the array will convert to [1,8,6]. Return the maximum length of a non-decreasing array that can be made after applying operations. A subarray is a contiguous non-empty sequence of elements within an array.

class Solution:
    def findMaximumLength(self, nums: list[int]) -> int:
        left, mid, right = 0,0,0


s = Solution()

nums = [5,2,2]
print(s.findMaximumLength(nums))
nums = [1,2,3,4]
print(s.findMaximumLength(nums))
nums = [4,3,2,6]
print(s.findMaximumLength(nums))
