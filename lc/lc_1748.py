# Leetcode Problem #1748: Sum of Unique Elements

# Description: You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array. Return the sum of all the unique elements of nums.

class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        h = {}
        ans = 0
        for num in nums:
            if num in h:
                ans -= num * h[num]
                h[num] = 0
            else:
                h[num] = 1
                ans += num
        return ans

s = Solution()

nums = [1,2,3,2]
print(s.sumOfUnique(nums))
nums = [1,1,1,1,1]
print(s.sumOfUnique(nums))

nums = [1,2,3,4,5]
print(s.sumOfUnique(nums))
