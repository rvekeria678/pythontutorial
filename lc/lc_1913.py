# Leetcode Problem #1913: Maximum Product Difference Between Two Pairs

# Description: The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d). For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16. Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized. Return the maximum such product difference.

class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        nums.sort()
        return (nums[len(nums)-1] * nums[len(nums)-2]) - (nums[0] * nums[1])

s = Solution()

nums1 = [5,6,2,7,4]

nums2 = [4,2,5,9,7,4,8]

print(s.maxProductDifference(nums1))
print(s.maxProductDifference(nums2))