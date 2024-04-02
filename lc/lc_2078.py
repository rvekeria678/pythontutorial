# Leetcode Problem #2078: Two Furthest Houses With Different Colors:

# Description: There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house. Return the maximum distance between two houses with different colors. The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.

class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        left, right = 0, len(colors)-1
        rev_colors = colors[::-1]
        while left < right:
            if colors[left] != colors[right] or rev_colors[left] != rev_colors[right]:
                return right - left
            else:
                right -= 1
        return 0

s = Solution()

colors = [1,1,1,6,1,1,1]
print(s.maxDistance(colors))

colors = [1,8,3,8,3]
print(s.maxDistance(colors))

colors = [0,1]
print(s.maxDistance(colors))
