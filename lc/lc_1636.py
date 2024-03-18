# Leetcode Problem #1636: Sort Array by Increasing Frequency

# Description: Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order. Return the sorted array.

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        d = {}
        res = []
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        freq = sorted(d, key=lambda x:d[x])
        for x in freq:
            temp = [x] * d[x]
            res += temp
        return res

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        temp, frequency = {}, {}
        for num in nums:
            if num in temp:
                temp[num] += 1
            else:
                temp[num] = 1
            if temp[num] in frequency:
                frequency[temp[num]].append(num)
                if temp[num]-1 in frequency:
                    frequency[temp[num]-1].remove(num)
            else:
                frequency[temp[num]] = [num]
                if temp[num]-1 in frequency:
                    frequency[temp[num]-1].remove(num)
        res = []
        for freq in frequency:
            values = sorted(frequency[freq], reverse=True)
            for val in values:
                temp = [val] * freq
                res += temp

        return res
    
s = Solution()

nums = [1,1,2,2,2,3]
print(s.frequencySort(nums))

nums = [2,3,1,3,2]
print(s.frequencySort(nums))

nums = [-1,1,-6,4,5,-6,1,4,1]
print(s.frequencySort(nums))
