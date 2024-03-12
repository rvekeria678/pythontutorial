# Leetcode Problem #3005: Count Elements with Maximum Frequency

# Description: You are given an array nums consisting of positive integers. Return the total frequencies of elements in nums such that those elements all have the maximum frequency. The frequency of an element is the number of occurrences of that element in the array.

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        frequencies = {}
        temp = {}
        last_added = 1
        for num in nums:
            if num in temp:
                temp[num] += 1
            else:
                temp[num] = 1
            if temp[num] in frequencies:
                frequencies[temp[num]] += 1
            else:
                frequencies[temp[num]] = 1
                last_added = temp[num]

        return last_added * frequencies[last_added]

s = Solution()

nums = [1,2,2,3,1,4]
print(s.maxFrequencyElements(nums))

nums = [1,2,3,4,5]
print(s.maxFrequencyElements(nums))
