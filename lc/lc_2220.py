# Leetcode Problem #2220: Minimum Bit Flips to Convert Number

# Description: A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0. For example, for x = 7, the binary representation is 111 and we may choose any bit (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get 110, flip the second bit from the right to get 101, flip the fifth bit from the right (a leading zero) to get 10111, etc. Given two integers start and goal, return the minimum number of bit flips to convert start to goal.

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        start ^= goal
        while start:
            if start & 1:
                count += 1
            start >>= 1
        return count

s = Solution()

start = 10
goal = 7
print(s.minBitFlips(start, goal))

start = 3
goal = 4
print(s.minBitFlips(start, goal))

