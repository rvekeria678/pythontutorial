# Leetcode Problem #807: Max Increase to Keep City Skyline

# Description: There is a city composed of n x n blocks, where each block contains a single building shaped like a vertical square prism. You are given a 0-indexed n x n integer matrix grid where grid[r][c] represents the height of the building located in the block at row r and column c. A city's skyline is the outer contour formed by all the building when viewing the side of the city from a distance. The skyline from each cardinal direction north, east, south, and west may be different. We are allowed to increase the height of any number of buildings by any amount (the amount can be different per building). The height of a 0-height building can also be increased. However, increasing the height of a building should not affect the city's skyline from any cardinal direction. Return the maximum total sum that the height of the buildings can be increased by without changing the city's skyline from any cardinal direction.

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        alt = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                
                pass
        return alt
s = Solution()

grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(s.maxIncreaseKeepingSkyline(grid))
grid = [[0,0,0],[0,0,0],[0,0,0]]
print(s.maxIncreaseKeepingSkyline(grid))



