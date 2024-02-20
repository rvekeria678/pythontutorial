# Leetcode Problem #1637: Widest Vertical Area Between Two Points Containing No Points

# Description: Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

# Note that points on the edge of a vertical area are not considered included in the area.

class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        x_values = sorted([point[0] for point in points])
        p, max = 0,0

        while p + 1 < len(x_values):
            if x_values[p + 1] - x_values[p] > max:
                max = x_values[p + 1] - x_values[p]
            p += 1
        return max
        


s = Solution()

l1 = [[8,7],[9,9],[7,4],[9,7]]
l2 = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]

print(s.maxWidthOfVerticalArea(l1))
print(s.maxWidthOfVerticalArea(l2))