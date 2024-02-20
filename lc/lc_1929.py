# Leetcode Problem #1929: Concatenation of Array

# Description: Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i+n] == nums[i] for 0 <= i < n (0-indexed). Specifically, ans is the concatenation of two nums arrays

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return 2 * nums
    
class Solution2:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            ans.insert(i, nums[i])
            ans.insert(len(nums)+i, nums[i])
        return ans

s = Solution()
s2 = Solution2()

l1 = [1,2,1]
l2 = [1,3,2,1]

print(s2.getConcatenation(l1))
print(s2.getConcatenation(l2))