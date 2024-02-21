# Leetcode Problem #169: Majority Element

# Description: Given an array nums of size n, return the majority element

# The majority element is the element that appears more that [n/2] times. You may assume that the majority element always exists in the array

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        curr, tally = 0,0
        for i in nums:
            if tally == 0:
                curr = i
            tally = tally+1 if curr==i else tally-1
        return curr

s = Solution()

l1 = [3,2,3]
l2 = [2,2,1,1,1,2,2]

print(s.majorityElement(l1))
print(s.majorityElement(l2))