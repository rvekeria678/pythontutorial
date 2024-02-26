# Leetcode Problem #709: To Lower Case

# Description: Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

s = Solution()

str1 = "Hello"
print(s.toLowerCase(str1))

str2 = "here"
print(s.toLowerCase(str2))

str3 = "LOVELY"
print(s.toLowerCase(str3))