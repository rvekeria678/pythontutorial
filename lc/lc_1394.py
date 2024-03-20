# Leetcode Problem #1394: Find Lucky Integer in an Array

# Description: Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value. Return the largest lucky integer in the array. If there is no lucky integer return -1.

class Solution:
    def findLucky(self, arr: list[int]) -> int:
        d = {}
        m = -1
        for num in arr:
            if num in d:
                d[num] += 1 
            else:
                d[num] = 1
        for num in d:
            if num == d[num]:
                m = max(m, num)
        return m

s = Solution()

arr = [2,2,3,4]
print(s.findLucky(arr))

arr = [1,2,2,3,3,3]
print(s.findLucky(arr))

arr = [2,2,2,3,3]
print(s.findLucky(arr))
