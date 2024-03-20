# Leetcode Problem #268: Missing Number

# Description: Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i

class Solution2:
    def missingNumber(self, nums: list[int]) -> int:
        size = len(nums)
        count = 0
        for i in range(size):
            count += nums[i]
        return ((size * (size + 1)) // 2) - count

class Solution3:
    def missingNumber(self, nums: list[int]) -> int:
        x = 0
        y = 0
        last = 0
        for i in range(len(nums)):
            x ^= i
            y ^= nums[i]
            last = i
        return x ^ (last+1) ^ y

s = Solution()
s2 = Solution2()
s3 = Solution3()

nums = [3,0,1]
print(s3.missingNumber(nums))

nums = [0,1]
print(s3.missingNumber(nums))

nums = [9,6,4,2,3,5,7,0,1]
print(s3.missingNumber(nums))
