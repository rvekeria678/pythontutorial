# Leetcode Problem #2215: Find the Difference of Two Arrays

# Description: Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where: answer[0] is a list of all distinct integers in nums1 which are not present in nums2, answer[1] is a list of all distinct integers in nums2 which are not present in nums1. Note that the integers in the lists may be returned in any order.

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        h1, h2 = {}, {}
        ans1, ans2 = [], []
        for num in nums1:
            if num not in nums2 and num not in h1:
                ans1.append(num)
                h1[num] = 1
        for num in nums2:
            if num not in nums1 and num not in h2:
                ans2.append(num)
                h2[num] = 1

        return [ans1, ans2]  
    
class Solution2:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        s1, s2 = set(nums1), set(nums2)
        return [list(s1-s2), list(s2-s1)]


s = Solution()
s2 = Solution2()

nums1 = [1,2,3]
nums2 = [2,4,6]
print(s2.findDifference(nums1, nums2))

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(s2.findDifference(nums1, nums2))