# Leetcode Problem #338: Counting Bits

# Description: Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = []
        for i in range(n+1):
            ans.append(str(bin(i)).count('1'))
        return ans
# Dynamic Programming Solution    
class Solution2:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n+1)
        for i in range(1, n+1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans

s = Solution()
s2 = Solution2()

n = 2
print(s2.countBits(n))

n = 5
print(s2.countBits(n))

# 0 - 0 0 0 0 : 0
# 1 - 0 0 0 1 : 1
# 2 - 0 0 1 0 : 1
# 3 - 0 0 1 1 : 2

# 4 - 0 1 0 0 : 1 <- 1 + dp[n-4] 
# 5 - 0 1 0 1 : 2 <- 1 + dp[n-4]
# 6 - 0 1 1 0 : 2 <- 1 + dp[n-4]
# 7 - 0 1 1 1 : 3 <- 1 + dp[n-4]

# 8 - 1 0 0 0 : 1 <- 1 + dp[n-8]
# 9 - 1 0 0 1 : 2 <- 1 + dp[n-8]
#10 - 1 0 1 0 : 2 <- 1 + dp[n-8]
#11 - 1 0 1 1 : 3 <- 1 + dp[n-8]

#12 - 1 1 0 0 : 2 <- 1 + dp[n-8]
#13 - 1 0 1 1 : 3 <- 1 + dp[n-8]
#14 - 1 1 1 0 : 3 <- 1 + dp[n-8]
#15 - 1 1 1 1 : 4 <- 1 + dp[n-8]


