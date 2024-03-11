# Leetcode Problem #496: Next Greater Element I

# Description: The next greater element of some element x in an array is the first greater element that is to the right of x in the same array. You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2. For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1. Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums1)):
            res = -1
            for j in range(nums2.index(nums1[i]),len(nums2)):
                if nums2[j] > nums1[i]:
                    res = j
                    break
            if res != -1:
                ans.append(nums2[res])
            else:
                ans.append(res)
        return ans
    
s = Solution()

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(s.nextGreaterElement(nums1,nums2))

nums1 = [2,4]
nums2 = [1,2,3,4]
print(s.nextGreaterElement(nums1,nums2))

