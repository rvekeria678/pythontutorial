# Leetcode Problem #35: Search Insert Position

# Description: Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were insterted in order. The algorithm should be in O(log n) runtime complexity

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if (nums[i] >= target):
                return i
        return len(nums)
    
s = Solution()

nums = [1,3,5,6]
target = 7

print(s.searchInsert(nums=nums, target=target))