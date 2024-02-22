# Leetcode Problem #2373: Largest Local Values in a Matrix

# Description: You are given an n x n integer matrix grid. Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that: maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1. In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid. Return the generated matrix.

class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
    #    for row in range(len(grid)):
    #        for col in range(len(grid)-2):
    #            print(grid[row][col:col+3])
        print(f'grid - {(grid[:3])[:2]}')

s = Solution()

grid1 = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
grid2 = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]

print(s.largestLocal(grid1))
print(s.largestLocal(grid2))