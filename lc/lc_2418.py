# Leetcode Problem #2418: Sort the People

# Description: You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n. For each index i, names[i] and heights[i] denote the name and height of the ith person. Return names sorted in descending order by the people's heights.

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        for i in range(1,len(heights)):
            j = i - 1
            while j >= 0 and heights[i] < heights[j]:
                j-=1
            
                


s = Solution()

names = ["Mary","John","Emma"]
heights = [180,165,170]

print(s.sortPeople(names,heights))

names = ["Alice","Bob","Bob"]
heights = [155,185,150]
print(s.sortPeople(names, heights))

