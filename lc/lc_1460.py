# Leetcode Problem #1460: Make Two Arrays Equal by Reversing Subarrays

# Description: You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps. Return true if you can make arr equal to target or false otherwise.

class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        target = sorted(target)
        arr = sorted(arr)

        for i in range(len(target)):
            if target[i] != arr[i]:
                return False
        return True
    
s = Solution()

target = [1,2,3,4]
arr = [2,4,1,3]
print(s.canBeEqual(target, arr))

target = [7]
arr = [7]
print(s.canBeEqual(target, arr))

target = [3,7,9]
arr = [3,7,11]
print(s.canBeEqual(target, arr))

