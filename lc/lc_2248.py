# Leetcode Problem #2248: Intersection of Multiple Arrays

# Description: Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.

class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        frequency = {}
        res = []
        for row in nums:
            for element in row:
                if element in frequency:
                    frequency[element] += 1
                else:
                    frequency[element] = 1
        for element in frequency:
            if frequency[element] == len(nums):
                res.append(element)
        return sorted(res)

s = Solution()

nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
print(s.intersection(nums))

nums = [[1,2,3],[4,5,6]]
print(s.intersection(nums))
