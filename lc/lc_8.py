# Leetcode Problem #8: String to Integer(atoi)

# Description: Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer(similar to C/C++ atoi function).

class Solution:
    def myAtoi(self, s: str) -> int:
        num = ''
        lower = -2 ** 31
        upper = 2 ** 31 - 1
        for i in s:
            if i.isalpha() and not len(num):
                return 0
            elif not i.isnumeric() and len(num):
               break
            elif not i.isspace():
                num += i
        num = 0 if not len(num) or num == '+' or num == '-' else int(float(num))
        if num < lower:
            return lower
        elif num > upper:
            return upper
        return num

s = Solution()

print('result:',s.myAtoi("42"))

print('result: ',s.myAtoi("    -42"))

print('result:',s.myAtoi("4193 with words"))

print('result:',s.myAtoi('-91283472332'))

print('result:',s.myAtoi('3.14159265'))

print('result:', s.myAtoi('+-12'))