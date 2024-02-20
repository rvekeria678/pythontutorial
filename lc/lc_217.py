# Leetcode Problem #217: Contains Duplicate

# Description: Given an integer array nums, return true if any value appears at least twice in the array, and false if every element is distinct.
from functools import reduce

class Solution:
    def containsDuplicates(self, nums: list[int]) -> bool:
        dict = {}
        for i in nums:
            if i in dict:
                return True
            dict[i] = ''
        return False

s = Solution()

l1 = [1,2,3,1]
l2 = [1,2,3,4]
l3 = [1,1,1,3,3,4,3,2,4,2]
l4 = [0]

print(s.containsDuplicates(l1))
print(s.containsDuplicates(l2))
print(s.containsDuplicates(l3))
print(s.containsDuplicates(l4))