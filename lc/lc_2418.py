# Leetcode Problem #2418: Sort the People

# Description: You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n. For each index i, names[i] and heights[i] denote the name and height of the ith person. Return names sorted in descending order by the people's heights.

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        d = {}
        res = []
        for i in range(len(heights)):
            d[heights[i]] = names[i]

        d = dict(sorted(d.items(), reverse=True))

        for i in d:
            res.append(d[i])

        return res
            
                


s = Solution()

names = ["Mary","John","Emma"]
heights = [180,165,170]

print(s.sortPeople(names,heights))

names = ["Alice","Bob","Bob"]
heights = [155,185,150]
print(s.sortPeople(names, heights))

