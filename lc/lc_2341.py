# Leetcode Problem #2341: Maximum Number of Pairs in Array

# Description: You are given a 0-indexed integer array nums. In one operation, you may do the following: Choose two integers in nums that are equal, Remove both integers from nums, forming a pair. The operation is done on nums as many times as possible. Return a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs that are formed and answer[1] is the number of leftover integers in nums after doing the operation as many times as possible.

class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        d = {}
        numPairs, numLeft = 0, 0
        for num in nums:
            if num in d: d[num] += 1
            else: d[num] = 1
        for num in d:
            numPairs += d[num] // 2
            numLeft += d[num] % 2
        return [numPairs, numLeft]

s = Solution()

nums = [1,3,2,1,3,2,2]
print(s.numberOfPairs(nums))

nums = [1,1]
print(s.numberOfPairs(nums))

nums = [0]
print(s.numberOfPairs(nums))
