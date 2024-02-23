# Leetcode Problem #2913: Subarrays Distinct Element Sum of Squares I

# Description: You are given a 0-indexed integer array nums. The distinct count of a subarray of nums is defined as: Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j]. Return the sum of the squares of distinct counts of all subarrays of nums. A subarray is a contiguous non-empty sequence of elements within an array.

class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        left, right, res = 0,1,0

        while left <= len(nums) - 1:
            res += len(set(nums[left:right]))**2
            if right >= len(nums):
                left += 1
                right = left
            right += 1
        return res

s = Solution()

nums1 = [1,2,1]
nums2 = [1,1]

print(s.sumCounts(nums1))
print(s.sumCounts(nums2))

