# Leetcode Problem #2154: Keep Multiplying Found Values by Two

# Description: You are given an array of integers nums. You are also given an integer original which is the first number that needs to be searched for in nums. You then do the following steps: If original is found in nums, multiply it by two (i.e., set original = 2 * original), Otherwise, stop the process, Repeat this process with the new number as long as you keep finding the number. Return the final value of original.

class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        d = set(nums)
        while original in d:
            original *= 2
        return original

s = Solution()

nums = [5,3,6,1,12]
original = 3
print(s.findFinalValue(nums, original))

nums = [2,7,9]
original = 4
print(s.findFinalValue(nums, original))
