# Leetcode Problem #2032: Two Out of Three

# Description: Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.

class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        h = {}
        res = []
        for n in nums1: 
            if n not in h: h[n] = 1
        for n in nums2: 
            if n not in h: h[n] = 1
        for n in nums3: 
            if n not in h: h[n] = 1
        for n in h:
            if (n in nums1 and n in nums2) or (n in nums2 and n in nums3) or (n in nums1 and n in nums3):
                res.append(n)
        return res

s = Solution()
        
nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
print(s.twoOutOfThree(nums1, nums2, nums3))

nums1 = [3,1]
nums2 = [2,3]
nums3 = [1,2]
print(s.twoOutOfThree(nums1, nums2, nums3))

nums1 = [1,2,2]
nums2 = [4,3,3]
nums3 = [5]
print(s.twoOutOfThree(nums1, nums2, nums3))
