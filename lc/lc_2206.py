# Leetcode Problem #2206: Divide Array Into Equal Pairs

# Description: You are given an integer array nums consisting of 2 * n integers. You need to divide nums into n pairs such that: Each element belongs to exactly one pair, The elements present in a pair are equal. Return true if nums can be divided into n pairs, otherwise return false.

class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        d = {}
        size = len(nums)
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        for num in d:
            if d[num] % (size/(size/2)):
                return False
        return True

s = Solution()

nums = [3,2,3,2,2,2]
print(s.divideArray(nums))
nums = [1,2,3,4]
print(s.divideArray(nums))
