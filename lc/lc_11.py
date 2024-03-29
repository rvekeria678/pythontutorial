# Leetcode Problem #11: Container with Most Water

# Description: You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store. Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right, size = 0, 1, len(height)
        maximum_volume = 0
        while left < size-1:
            maximum_volume = max(min(height[left], height[right]) * (right - left), maximum_volume)
            if right >= size-1:
                left += 1
                right = left
            right += 1
        return maximum_volume        
               
class Solution2:
    def maxArea(self, height: list[int]) -> int:
        size = len(height)
        maxVolume = 0
        for i in range(size):
            for j in range(i+1, size):
                maxVolume = max(min(height[i], height[j])* (j-i), maxVolume)
        return maxVolume
    
class Solution3:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        m = 0
        while left < right:
            x = abs(right-left)
            y = min(height[left], height[right])
            m = max(m, x * y)

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return m

s = Solution()
s2 = Solution2()
s3 = Solution3()

height = [1,8,6,2,5,4,8,3,7]
print(s3.maxArea(height))

height = [1,1]
print(s3.maxArea(height))

# Basic Logic: Find the largest value in [] with indicies that are furthest apart

# Start at ends, move towards center