# Leetcode Problem #1534: Count Good Triplets

# Description: Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets. A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true: 0 <= i < j < k < arr.length; |arr[i] - arr[j]| <= a; |arr[j] - arr[k]| <= b; |arr[i] - arr[k]| <= c. Where |x| denotes the absolute value of x. Return the number of good triplets.

class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        left, mid, right, res = 0,1,2,0
        while left < len(arr)-2:
            if (abs(arr[left]-arr[mid]) <= a)and(abs(arr[mid]-arr[right]) <= b)and(abs(arr[left]-arr[right]) <= c):
                res += 1
            if right < len(arr)-1:
                right += 1
            elif mid < len(arr)-2:
                mid += 1
                right = mid + 1
            else:
                left += 1
                mid = left + 1
                right = mid + 1
        return res

s = Solution()

arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
print(s.countGoodTriplets(arr,a,b,c))

arr = [1,1,2,2,3]
a = 0
b = 0
c = 1
print(s.countGoodTriplets(arr,a,b,c))



