# Leetcode Problem #1403: Minimum Subsequence in Non-Increasing Order

# Description: Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements in such subsequence. If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions, return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array. Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in non-increasing order.

class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums = sorted(nums, reverse=True)
        minimum_subseqeunce = []
        limit = sum(nums) // 2
        running_total = 0
        for num in nums:
            running_total += num
            if running_total <= limit:
                minimum_subseqeunce.append(num)
            else:
                minimum_subseqeunce.append(num)
                break
        return minimum_subseqeunce
       
s = Solution()

nums = [4,3,10,9,8]
print(s.minSubsequence(nums))

nums = [4,4,7,6,7]
print(s.minSubsequence(nums))
