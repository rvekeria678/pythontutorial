# Leetcode Problem #8: String to Integer(atoi)

# Description: Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer(similar to C/C++ atoi function).

class Solution:
    def myAtoi(self, s: str) -> int:
        n_flag = False
        for i in range(len(s)):
            