# Leetcode Problem #26: Remove Duplicates from Sorted Array

# Description: Given an integer array 'nums', sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums. Consider the number of unique elements of 'nums' to be 'k', everything after is irrelevant

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if (nums[k] != nums[i]):
                k += 1
                nums[k] = nums[i]
        print(nums)
        return k + 1
    
arr = [1,1,2]
s = Solution()

print(s.removeDuplicates(nums=arr))