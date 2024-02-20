# Leetcode Problem #202: Happy Number

# Description: Write an algorithm to determine if a number n is happy

class Solution:
    def isHappy(self, n: int) -> bool:
        n_str = str(n)
        res = 0

        if (n==1):
            return True
        elif (n < 1):
            return False
        elif (n > 2 ** 32 - 1):
            return False

        for i in range(len(n_str)):
            res += int(n_str[i]) ** 2
    
        return self.isHappy(res)




s = Solution()

print(s.isHappy(19))
print(s.isHappy(2))