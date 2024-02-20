# Leetcode Problem #1920: Build Array from Permutation

# Description: Given a zero-base permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return k. A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive)

class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans

s = Solution()

l1 = [0,2,1,5,3,4]
l2 = [5,0,1,2,3,4]

print(s.buildArray(l1))
print(s.buildArray(l2))