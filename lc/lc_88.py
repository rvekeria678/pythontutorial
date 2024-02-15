# Leetcode Problem #88: Merge Sorted Array

# Description: Give two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing order. The final sorted array should not be returned by the function, but instead be stored inside array nums1. To accomodate this, nums1 has a length of m + n, where the first m elements denote the elemts that should be merged, and the last n elements are set to 0 and should be ignored. nums has a length of n.

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        temp = []
        p1 = 0
        p2 = 0
        while p1 < m or p2 < n:
            if (p1 < m and nums1[p1] < nums2[p2]):
                temp.append(nums1[p1])
                p1 += 1
            else:
                temp.append(nums2[p2])
                p2 += 1
        nums1 = temp
        print(nums1)

    def merge2(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1 = nums1 + nums2
        print(nums1)

s = Solution()

arr1 = [1,2,3,0,0,0]
arr2 = [2,5,6]
arr3 = []

s.merge(arr1,3,arr2,3)

s.merge(arr1,3,arr3,0)