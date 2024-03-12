# Leetcode Problem #2670: Find the Distinct Difference Array

# Description: You are given a 0-indexed array nums of length n. The distinct difference array of nums is an array diff of length n such that diff[i] is equal to the number of distinct elements in the suffix nums[i + 1, ..., n - 1] subtracted from the number of distinct elements in the prefix nums[0, ..., i]. Return the distinct difference array of nums. Note that nums[i, ..., j] denotes the subarray of nums starting at index i and ending at index j inclusive. Particularly, if i > j then nums[i, ..., j] denotes an empty subarray.

class Solution:
    def distinctDifferenceArray(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(len(set(nums[:i+1])) - len(set(nums[i+1:])))
        return ans

s = Solution()

nums = [1,2,3,4,5]
print(s.distinctDifferenceArray(nums))

nums = [3,2,3,4,2]
print(s.distinctDifferenceArray(nums))
