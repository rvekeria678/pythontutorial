# Leetcode Problem #238: Product of Arry Except Self

# Description: Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operation.

from functools import reduce

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        x = reduce(lambda a,b: a*b, nums)
        ans = []
        for i in range(len(nums)):
            if nums[i]:
                ans.append(x // nums[i])
            else:
                ans.append(1)
                if nums[:i]:
                    ans[i] *= reduce(lambda a,b: a*b, nums[:i])
                if nums[i+1:]:
                    ans[i] *= reduce(lambda a,b: a*b, nums[i+1:])
        return ans

s = Solution()    

nums = [1,2,3,4]
print(s.productExceptSelf(nums))

nums = [-1,1,0,-3,3]
print(s.productExceptSelf(nums))
