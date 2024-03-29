# Leetcode Problem #1827: Minimum Operations to Make the Array Increasing

# Description: You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment it by 1. For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3]. Return the minimum number of operations needed to make nums strictly increasing. An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array of length 1 is trivially strictly increasing.

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        operations = 0
        size = len(nums)
        if size == 1: return operations
        for i in range(1,size):
            while nums[i] <= nums[i-1]:
                nums[i] += 1
                operations += 1
        return operations
    
class Solution2:
    def minOperations(self, nums: list[int]) -> int:
        operations = 0
        size = len(nums)
        if size == 1: return operations
        for i in range(1,size):
            if nums[i] <= nums[i-1]:
                operations += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1] + 1
        return operations

s = Solution()
s2 = Solution2()

nums = [1,1,1]
print(s2.minOperations(nums))

nums = [1,5,2,4,1]
print(s2.minOperations(nums))

nums = [8]
print(s2.minOperations(nums))
