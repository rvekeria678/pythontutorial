# Leetcode Problem #922: Sort Array By Parity II

# Description: Given an array of integers nums, half of the integers in nums are odd, and the other half are even. Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even. Return any answer array that satisfies this condition.

class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        even, odd, res = [], [], []
        for i in nums:
            if i % 2:
                odd.append(i)
            else:
                even.append(i)
        
        for i in range(len(even)):
            res.append(even[i])
            res.append(odd[i])
        
        return res


s = Solution()

nums = [4,2,5,7]
print(s.sortArrayByParityII(nums))
nums = [2,3]
print(s.sortArrayByParityII(nums))
