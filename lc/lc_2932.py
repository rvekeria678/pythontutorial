# Leetcode Problem #2932: Maximum Strong Pair XOR I

# Description: You are given a 0-indexed integer array nums. A pair of integers x and y is called a strong pair if it satisfies the condition: |x - y| <= min(x, y). You need to select two integers from nums such that they form a strong pair and their bitwise XOR is the maximum among all strong pairs in the array. Return the maximum XOR value out of all possible strong pairs in the array nums. Note that you can pick the same integer twice to form a pair.

class Solution: # Brute Force Approach
    def maximumStrongPairXor(self, nums: list[int]) -> int:
        mxp = 0
        for num1 in nums:
            for num2 in nums:
                if abs(num1-num2) <= min(num1, num2):
                    mxp = max(mxp, num1^num2)
        return mxp
        
class Solution2: # Binary Search
    def maximumStrongPairXor(self, nums: list[int]) -> int:
        nums = sorted(nums)
        mxp = 0
        for i in range(len(nums)):
            j = i
            x = nums[i] // 2 + 1 if nums[i] % 2 else nums[i] / 2
            while j >= 0 and nums[j] >= x:
                mxp = max(mxp, nums[j]^nums[i])
                j -= 1
        return mxp

s = Solution()
s2 = Solution2()

nums = [1,2,3,4,5]
print(s2.maximumStrongPairXor(nums))

nums = [10,100]
print(s2.maximumStrongPairXor(nums))

nums = [5,6,25,30]
print(s2.maximumStrongPairXor(nums))
