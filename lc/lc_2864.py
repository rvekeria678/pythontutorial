# Leetcode Problem #2864: Maximum Odd Binary Number

# Description: You are given a binary string s that contains at least one '1'. You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination. Return a string representing the maximum odd binary number that can be created from the given combination. (Note that the resulting string can have leading zeros.)

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        size = len(s)
        number_of_ones = s.count('1')
        return '1' * (number_of_ones - 1) + '0' * (size - number_of_ones) + '1'

s = Solution()

st = "010"
print(s.maximumOddBinaryNumber(st))

st = "0101"
print(s.maximumOddBinaryNumber(st))
