# Leetcode Problem #1486: Operation in an Array

# Description: You are given an integer n and an integer start. Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length. Return the bitwise XOR of all elements of nums.

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            res ^= start + 2 * i
        return res

s = Solution()

n = 5
start = 0
print(s.xorOperation(n, start))

n = 4
start = 3
print(s.xorOperation(n, start))
