# Leetcode Problem #1844: Replace All Digits with Characters

# Description: You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices. There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'. For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]). Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.

class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ''
        for c in s:
            if c.isdigit():
                res += chr(ord(res[len(res)-1])+int(c))
            else:
                res += c
        return res

s = Solution()

str1 = "a1c1e1"
str2 = "a1b2c3d4e"

print(s.replaceDigits(str1))
print(s.replaceDigits(str2))

