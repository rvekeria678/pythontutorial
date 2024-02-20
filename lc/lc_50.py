# Leetcode Problem #50: Pow(x,n)

# Description: Implement pow(x,n) which calculates x raised to the power n (i.e.,x^n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n < 0:
            x = 1/x
            n = abs(n)
        for i in range(n):
            res *= x
        return res
    
class Solution2:
    def myPow(self, x: float, n: int) -> float:
        return x ** n

s = Solution()
s2 = Solution2()

#print(s.myPow(2.00000, 10))
#print(s.myPow(2.10000, 3))
#print(s.myPow(2.00000, -2))

print(s2.myPow(2,10))
print(s2.myPow(3,3))
#print(s2.myPow(2.1,3))
#print(s2.myPow(2, -2))