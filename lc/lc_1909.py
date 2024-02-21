# Leetcode Problem #1909: Remove One Element to Make the Array Strictly Increasing

# Description: Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one element, or false otherwise. If the array is already strictly increasing, return true. The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).

class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:
        removed = False
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                if removed:
                    return False
                if i > 1 and nums[i] <= nums[i-2]:
                    nums[i] = nums[i-1] 
                removed = True
        return True
s = Solution()

l1 = [1,2,10,5,7]
l2 =[2,3,1,2]

print(s.canBeIncreasing(l1))
print(s.canBeIncreasing(l2))