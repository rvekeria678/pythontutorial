# Leetcode Problem #8: String to Integer(atoi)

# Description: Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer(similar to C/C++ atoi function).

class Solution:
    def myAtoi(self, s: str) -> int:
        num = ''
        r_flag = False
        upper = 2 ** 31 - 1
        lower = -2 ** 31
        for i in s:
            if not i.isalpha():
                num += i
                print(num)
                r_flag = True
            elif i.isalpha() and r_flag:
                num = int(num)
                if num > upper: 
                    return upper
                elif num < lower: 
                    return lower
                else: 
                    return num
        return 0
            
s = Solution()

print(s.myAtoi("Hello 1234 World"))

print(s.myAtoi("    -42"))