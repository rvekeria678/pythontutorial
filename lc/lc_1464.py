# Leetcode Problem #1464: Maximum Product of Two Elements in an Array

# Description: Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums.sort()
        return (nums[len(nums)-1]-1) * (nums[len(nums)-2]-1)

s = Solution()

nums1 = [3,4,5,2]
nums2 = [1,5,4,5]

print(s.maxProduct(nums1))
print(s.maxProduct(nums2))