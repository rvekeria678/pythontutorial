# Leetcode Problem #2824: Count Pairs Whose Sum is Less than Target

# Description: Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.

class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        left, right, count = 0, 1, 0

        if len(nums) == 1:
            return 0
        
        while left < len(nums) - 1:
            if right >= len(nums):
                left += 1
                right = left
            elif nums[right] + nums[left] < target:
                count += 1
            right += 1 

        return count

s = Solution()

l1 = [-1,1,2,3,1]
l2 = [-6,2,5,-2,-7,-1,3]

print(s.countPairs(l1,2))
print(s.countPairs(l2,-2))
