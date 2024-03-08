# Leetcode Problem #2200: Find All K-Distant Indicies in an Array

# Description: You are given a 0-indexed integer array nums and two integers key and k. A k-distant index is an index i of nums for which there exists at least one index j such that |i - j| <= k and nums[j] == key. Return a list of all k-distant indices sorted in increasing order.

class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        current, next = 0,0
        res = []
        size = len(nums)
        while next < size:
            if nums[next] == key:
                if next-current <= k and current < size:
                    res.append(current)
                if current >= next+k:
                    next += 1            
                current += 1
            else:
               next += 1
        return res        

s = Solution()

nums = [3,4,9,1,3,9,5]
key = 9
k = 1
print(s.findKDistantIndices(nums,key,k))

nums = [2,2,2,2,2]
key = 2
k = 2
print(s.findKDistantIndices(nums,key,k))
