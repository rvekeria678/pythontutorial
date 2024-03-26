# Leetcode Problem #128: Longest Consecutive Sequence

# Description: Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = sorted(list(set(nums)))
        print(nums)
        count = m = 1
        if len(nums) < 1: return 0
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                count += 1
            else:
                count = 1
            m = max(count, m)

        return m
    
class Solution2:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = {}
        count = m = 1
        if len(nums) < 1: return 0
        for num in nums:
            seen[num] = ''

        for num in seen:
            if num - 1 not in seen:
                while num + count in seen:
                    count += 1 
            m = max(m, count)
            count = 1
        return m
    
s = Solution()
s2 = Solution2()

nums = [100,4,200,1,3,2]
print(s2.longestConsecutive(nums))

nums = [0,3,7,2,5,8,4,6,0,1]
print(s2.longestConsecutive(nums))
