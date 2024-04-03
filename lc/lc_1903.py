# Leetcode Problem #1903: Largest Odd Number in String

# Description: You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists. A substring is a contiguous sequence of characters within a string.

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) % 2:
                return num[:i+1]
        return ""

s = Solution() 

num = "52"
print(s.largestOddNumber(num))

num = "4206"
print(s.largestOddNumber(num))

num = "35427"
print(s.largestOddNumber(num))
