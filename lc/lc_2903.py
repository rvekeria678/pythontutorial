# Leetcode Problem #2903: Find Indicies With Index and Value Difference I

# Description: You are given a 0-indexed integer array nums having length n, an integer indexDifference, and an integer valueDifference. Your task is to find two indices i and j, both in the range [0, n - 1], that satisfy the following conditions: abs(i - j) >= indexDifference, and abs(nums[i] - nums[j]) >= valueDifference. Return an integer array answer, where answer = [i, j] if there are two such indices, and answer = [-1, -1] otherwise. If there are multiple choices for the two indices, return any of them. (Note: i and j may be equal.)

class Solution:
    def findIndices(self, nums: list[int], indexDifference: int, valueDifference: int) -> list[int]:
        window = len(nums) - 1
        while window >= indexDifference:
            for i in range(len(nums)-window):
                if abs(nums[i]-nums[i+window] >= valueDifference):
                    return [i, i+window]          
            window -= 1
        return [-1,-1]

s = Solution()

nums = [5,1,4,1]
indexDifference = 2
valueDifference = 4
print(s.findIndices(nums, indexDifference, valueDifference))

nums = [2,1]
indexDifference = 0
valueDifference = 0
print(s.findIndices(nums, indexDifference, valueDifference))

nums = [1,2,3]
indexDifference = 2
valueDifference = 4
print(s.findIndices(nums, indexDifference, valueDifference))
