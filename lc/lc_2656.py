# Leetcode Problem #2656: Maximum Sum With Exactly K Elements

# Description: You are given a 0-indexed integer array nums and an integer k. Your task is to perform the following operation exactly k times in order to maximize your score: Select an element m from nums; Remove the selected element m from the array; Add a new element with a value of m + 1 to the array; Increase your score by m. Return the maximum score you can achieve after performing the operation exactly k times.

class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        largest = max(nums)
        res = 0
        for i in range(k):
            res += largest + i
        return res

s = Solution()

nums1 = [1,2,3,4,5]
k1 = 3
nums2 = [5,5,5]
k2 = 2

print(s.maximizeSum(nums1, k1))
print(s.maximizeSum(nums2, k2))