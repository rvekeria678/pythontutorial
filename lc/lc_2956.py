# Leetcode Problem #2956: Find Common Elements Between Two Arrays

# Description: You are given two 0-indexed integer arrays nums1 and nums2 of sizes n and m, respectively. Consider calculating the following values: The number of indices i such that 0 <= i < n and nums1[i] occurs at least once in nums2; The number of indices i such that 0 <= i < m and nums2[i] occurs at least once in nums1. Return an integer array answer of size 2 containing the two values in the above order.

class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        dict = {}
        count1 = 0
        count2 = 0
        for i in nums1:
            if i in nums2:
                count1 += 1
                if i not in dict:
                    dict[i] = 1
        for i in nums2:
            if i in dict:
                count2 += 1
        return [count1, count2]
    
class Solution2:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        s1 = set(nums1)
        s2 = set(nums2)

        c1 = sum(1 for num in nums1 if num in s2)
        c2 = sum(1 for num in nums2 if num in s1)

        return [c1,c2]

s = Solution()    
s2 = Solution2()

nums1 = [4,3,2,3,1]
nums2 = [2,2,5,2,3,6]
nums3 = [3,4,2,3]
nums4 = [1,5]

print(s.findIntersectionValues(nums1, nums2))
print(s.findIntersectionValues(nums3, nums4))

print('\nSolution 2:')
print(s.findIntersectionValues(nums1, nums2))
print(s.findIntersectionValues(nums1, nums2))