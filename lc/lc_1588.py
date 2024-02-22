# Leetcode Problem #1588: Sum of All Odd Length Subarrays

# Description: Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr. A subarray is a contiguous subsequence of the array.

class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        res, skip = 0,1
        while skip <= len(arr):
            for i in range(len(arr)-skip+1):
                res += sum(arr[i:i+skip])
            skip += 2
        return res
    
class Solution2: # Very Efficient Solution
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        res, freq, n = 0, 0, len(arr)
        for i in range(n):
            freq = freq-(i+1)//2+(n-i+1)//2
            print(f'frequency: {freq}, arr: {arr[i]}')
            res += freq * arr[i]
        return res


s = Solution()
s2 = Solution2()

arr1 = [1,4,2,5,3]
arr2 = [1,2]
arr3 = [10,11,12]

print(s.sumOddLengthSubarrays(arr1))
print(s.sumOddLengthSubarrays(arr2))
print(s.sumOddLengthSubarrays(arr3))

print('\n')

print(s2.sumOddLengthSubarrays(arr1))
print(s2.sumOddLengthSubarrays(arr2))
print(s2.sumOddLengthSubarrays(arr3))