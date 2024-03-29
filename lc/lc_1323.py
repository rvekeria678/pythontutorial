# Leetcode Problem #1323

# Description: You are given a positive integer num consisting only of digits 6 and 9. Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        for i in range(len(num)):
            if num[i] == '6':
                num = list(num)
                num[i] = '9'
                num = ''.join(num)
                break
        return int(num)
                

s = Solution()

num = 9669
print(s.maximum69Number(num))

num = 9996
print(s.maximum69Number(num))

num = 9999
print(s.maximum69Number(num))
