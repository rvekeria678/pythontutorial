# Leetcode Problem #202: Happy Number

# Description: Write an algorithm to determine if a number n is happy

class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        temp = n
        while n != 1:
            n = 0
            while temp > 0:
                n += (temp % 10) ** 2
                temp //= 10
            print(n)
            if n not in d:
                d[n] = '-'
            else:
                return False 
            temp = n
        return True



s = Solution()

print(s.isHappy(19))
print(s.isHappy(2))