# Leetcode Problem #12: Integer to Roman

 # Description: Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M. For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II. Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used: I can be placed before V (5) and X (10) to make 4 and 9, X can be placed before L (50) and C (100) to make 40 and 90, C can be placed before D (500) and M (1000) to make 400 and 900. Given an integer, convert it to a roman numeral.

class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1: 'I', 5: 'V', 10:'X', 50: 'L', 100: 'C', 500:'D', 1000:'M'}
        t = 0
        res = []
        while num:
            digit = num % 10
            roman_digit = ''
            while digit > 0:
                if digit == 4 or digit == 9:
                    roman_digit = d[10**t] + d[10**(t+1)] if digit == 9 else d[10**t] + d[5*10**t]
                    break
                elif digit >= 5:
                    roman_digit += d[5*10**t]
                    digit -= 5 
                else:
                    roman_digit += d[10**t]
                    digit -= 1
            res.append(roman_digit)
            num //= 10
            t += 1

        return ''.join(res[::-1])

                

s = Solution()

num = 3
print(s.intToRoman(num))

num = 58
print(s.intToRoman(num))

num = 1994
print(s.intToRoman(num))
