# Leetcode Problem #119: Pascal Triangle II

# Description: Given an integer rowIndex, return the rowIndex-th (0-indexed) row of the Pascal's triangle. In Pascal's triangle, each number is the sume of the two numbers directly above it.

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        res = [[1]]
        rowIndex += 1
        for i in range(rowIndex - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1])+1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res[-1]  

s = Solution()

print(s.getRow(3))