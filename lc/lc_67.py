# Leetcode Problem #67: Add Binary

# Description: Given two binary strings a and b, return their sum as a binary string

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x,y = int(a,2), int(b,2)
        return bin(int(a,2)+int(b,2))[2::]

s = Solution()

a = '11'
b = '1'

print(s.addBinary(a,b))