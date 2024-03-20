# Leetcode Problem #1331: Rank Transform of an Array

# Description: Given an array of integers arr, replace each element with its rank. The rank represents how large the element is. The rank has the following rules: Rank is an integer starting from 1. The larger the element, the larger the rank. If two elements are equal, their rank must be the same. Rank should be as small as possible.

class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        arr2 = sorted(list(set(arr)))
        ranks,rank = {},1
        for num in arr2:
            ranks[num] = rank
            rank += 1
        for i in range(len(arr)):
            arr[i] = ranks[arr[i]]

        return arr
            

s = Solution()

arr = [40,10,20,30]
print(s.arrayRankTransform(arr))

arr = [100,100,100]
print(s.arrayRankTransform(arr))

arr = [37,12,28,9,100,56,80,5,12]
print(s.arrayRankTransform(arr))
