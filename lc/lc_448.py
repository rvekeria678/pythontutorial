# Leetcode Problem #448: Find All Numbers Disappeared in an Array

# Description: Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        d = {}
        missing = []
        for num in nums:
            if num not in d:
                d[num] = ''
        for num in range(1,len(nums)+1):
            if num not in d:
                missing.append(num)
        return missing

s = Solution()
        
nums = [4,3,2,7,8,2,3,1]
print(s.findDisappearedNumbers(nums))

nums = [1,1]
print(s.findDisappearedNumbers(nums))