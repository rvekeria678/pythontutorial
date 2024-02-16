# Leetcode Problem #8: String to Integer(atoi)

# Description: Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer(similar to C/C++ atoi function).

class Solution:
    def myAtoi(self, s: str) -> int:
        num = ''
        r_flag = False
        upper = 2 ** 31 - 1
        lower = -2 ** 31
        for i in s:
            if i.isalpha() and not r_flag:
                break
            elif not i.isalpha() and not i.isspace():
                num += i
                r_flag = True
            elif i.isalpha() and r_flag:
                break

        
s = Solution()

#print(s.myAtoi("Hello 1234 World"))

#print(s.myAtoi("    -42"))

print(s.myAtoi("   3054 Hello World!"))

#print(s.myAtoi("   3.1415aef"))

#print(s.myAtoi("+-12"))