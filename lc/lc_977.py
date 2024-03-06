# Leetcode Problem #977: Square of a Sorted Array

# Description: Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted(list(map(lambda a : a ** 2, nums)))
    
class Solution2:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted([i ** 2 for i in nums])

s = Solution()
s2 = Solution2()

nums = [-4,-1,0,3,10]
print(s2.sortedSquares(nums))

nums = [-7,-3,2,3,11]
print(s2.sortedSquares(nums))
