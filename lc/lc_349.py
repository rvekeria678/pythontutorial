# Leetcode Problem #349: Intersection of Two Arrays

# Description: Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = {}
        for i in nums1:
            if i in nums2:
                res[i] = ''
        return list(res)

class Solution2:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        d = {}
        res = []
        for i in nums1:
            d[i] = ''
        for j in nums2:
            if j in d:
                res.append(j)
        return list(set(res))

s = Solution()
s2 = Solution2()

nums1 = [1,2,2,1]
nums2 = [2,2]
print(s2.intersection(nums1, nums2))

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(s2.intersection(nums1, nums2))
