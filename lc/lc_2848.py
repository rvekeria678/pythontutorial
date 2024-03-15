# Leetcode Problem #2848: Points That Intersect With Cars

# Description: You are given a 0-indexed 2D integer array nums representing the coordinates of the cars parking on a number line. For any index i, nums[i] = [starti, endi] where starti is the starting point of the ith car and endi is the ending point of the ith car. Return the number of integer points on the line that are covered with any part of a car.

class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        visited = {}
        for car in nums:
            while car[0] <= car[1]:
                if car[0] not in visited:
                    visited[car[0]] = ''
                car[0] += 1
        return len(visited)       

s =  Solution() 

nums = [[3,6],[1,5],[4,7]]
print(s.numberOfPoints(nums))
nums = [[1,3],[5,8]]
print(s.numberOfPoints(nums))