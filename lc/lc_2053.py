# Leetcode Problem #2053: Kth Distinct String in an Array

# Description: A distinct string is a string that is present only once in an array. Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "". Note that the strings are considered in the order in which they appear in the array.

class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        d = {}
        for s in arr:
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        for s in d:
            if d[s] == 1:
                if k == 1:
                    return s
                k -= 1
        return ''
    
s = Solution()

arr = ["d","b","c","b","c","a"]
k = 2
print(s.kthDistinct(arr,k))

arr = ["aaa","aa","a"]
k = 1
print(s.kthDistinct(arr,k))

arr = ["a","b","a"]
k = 3
print(s.kthDistinct(arr,k))
