# Leetcode Problem #2485: Find the Pivot Integer

# Description: Given a positive integer n, find the pivot integer x such that: The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively. Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

class Solution:
    def pivotInteger(self, n: int) -> int:
        left, right = 0, n
        lsum, rsum = 0, n
        while left < right:
            if lsum <= rsum:
                left += 1
                lsum += left
            elif lsum > rsum:
                right -= 1
                rsum += right
        return left if rsum == lsum else -1
        

s = Solution()

n = 8
print(s.pivotInteger(n))

n = 1
print(s.pivotInteger(n))

n = 4
print(s.pivotInteger(n))
