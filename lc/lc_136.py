# Leetcode Problem #136: Single Number

# Description: Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. The solution must be implemented with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: list[int],) -> int:
        hash = {}
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = i 
            else:
                hash.pop(nums[i])
                
        return int(*hash)
    
# XOR Solution
class Solution2:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for i in nums:
            result ^= i
        return result

s = Solution()
s2 = Solution2()

l1 = [2,2,1]
l2 = [4,1,2,1,2]
l3 = [1]

print(s2.singleNumber(l1))
print(s2.singleNumber(l2))
print(s2.singleNumber(l3))