# Leetcode Problem #1266: Minimum Time Visiting All Points

# Description: On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points. You can move according to these rules: move vertically by one unit, move horizontally by one unit, or move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).

class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        if len(points) < 2:
            return 1
        
        minimum_time = 0

        for i in range(len(points)-1):
            x_diff = abs(points[i+1][0] - points[i][0])
            y_diff = abs(points[i+1][1] - points[i][1])

            while x_diff or y_diff:
                if x_diff and y_diff:
                    x_diff -= 1
                    y_diff -= 1
                elif x_diff:
                    x_diff -= 1
                else:
                    y_diff -= 1
                minimum_time += 1
        return minimum_time
    
class Solution2:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        if len(points) < 2:
            return 1
        
        minimum_time = 0

        for i in range(len(points)-1):
            x_diff = abs(points[i+1][0] - points[i][0])
            y_diff = abs(points[i+1][1] - points[i][1])
            minimum_time += max(x_diff, y_diff)
            
        return minimum_time

s = Solution()
s2 = Solution2()

points1 = [[1,1],[3,4],[-1,0]]
points2 = [[3,2],[-2,2]]

print(s.minTimeToVisitAllPoints(points1))
print(s.minTimeToVisitAllPoints(points2))

print(s2.minTimeToVisitAllPoints(points1))
print(s2.minTimeToVisitAllPoints(points2))
