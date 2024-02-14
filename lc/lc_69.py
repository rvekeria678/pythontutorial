# Leetcode Problem #69: Sqrt(x)

# Description: Give a non-negative integer 'x', return the square root of 'x' rounded down to the nearest integer. The returned integer should be non-negative as well.

class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        while (start<=end):
            middle = (start + end)//2
            if middle * middle == x:
                return middle 
            elif middle * middle > x:
                end = middle - 1
            else:
                start = middle + 1
        return end
    
s = Solution()

print(s.mySqrt(0))
print(s.mySqrt(1))
print(s.mySqrt(4))
print(s.mySqrt(8))
print(s.mySqrt(9))