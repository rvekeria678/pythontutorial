# Leetcode Problem #1742: Maximum Number of Balls in a Box

# Description: You are working a ball factory where you have n balls numbered from lowLimit up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity. Your job at this factory is to put each ball in the box with a number equal to the sume of digits f the ball's number. For example, the ball number '321' will be put in the box number 3 + 2 + 1 = 6 and the ball number '10' will be put in the box number 1 + 0 = 1. Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}
        maxBox = 0
        for i in range(lowLimit, highLimit+1):
            box = 0
            temp = i
            while temp:
                box += temp % 10
                temp //= 10
            if box in boxes:
                boxes[box] += 1
            else:
                boxes[box] = 1
        for b in boxes:
            maxBox = max(maxBox, boxes[b])
        return maxBox


s = Solution()

lowLimit = 1
highLimit = 10
print(s.countBalls(lowLimit, highLimit))

lowLimit = 5
highLimit = 15
print(s.countBalls(lowLimit, highLimit))

lowLimit = 19
highLimit = 28
print(s.countBalls(lowLimit, highLimit))
