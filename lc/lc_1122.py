# Leetcode Problem #1122: Relative Sort Array

# Description: Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1. Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        frequency = {}
        misc = []
        res = []
        for num in arr1:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
            if num not in arr2:
                misc.append(num)
        for num in arr2:
            res += [num] * frequency[num]
        return res + sorted(misc)

s = Solution()

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(s.relativeSortArray(arr1, arr2))

arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]
print(s.relativeSortArray(arr1, arr2))
