# Leetcode Problem #1965: Find Missing and Repeated Values

# Description: You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b. Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        d = {}
        repeated = 0
        tally = 0
        a = 0
        b = 0
        n = len(grid)
        for i in grid:
            for j in i:
                if j in d:
                    repeated = j
                else:
                    d[j] = ''
                    tally += j
                b += 1
                a += b
        return [repeated, abs(a-tally)]
    
s = Solution()

grid = [[1,3],[2,2]]
print(s.findMissingAndRepeatedValues(grid))

grid = [[9,1,7],[8,9,2],[3,4,6]]
print(s.findMissingAndRepeatedValues(grid))
