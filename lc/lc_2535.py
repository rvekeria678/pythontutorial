# Leetcode Problem # 2353: Difference Between Element Sum and Digit Sum of an Array

# Description: You are given a positive integer array nums. The element sum is the sum of all the elements in nums. The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums. Return the absolute difference between the element sum and digit sum of nums. Note that the absolute difference between two integers x and y is defined as |x - y|.

class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0
        for i in nums:
            digit_sum += self.getDigitSum(i)

        return abs(element_sum - digit_sum)

    def getDigitSum(self, num):
        val = 0
        while num > 0:
            val += num % 10
            num = int(num/10)
        return val
            
s = Solution()

nums1 = [1,15,6,3]
nums2 = [1,2,3,4]

print(s.differenceOfSum(nums1))
print(s.differenceOfSum(nums2))