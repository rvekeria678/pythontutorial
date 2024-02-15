# Leetcode Problem #70: Climbing Stairs

# Description: You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int: # Recursive Solution
        if n <= 2:
            return n
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairs2(self, n: int) -> int:
        steps = 0
        p1 = 1
        p2 = 0
        for i in range(0, n):
            steps = p1 + p2
            p2 = p1
            p1 = steps
        return steps
    
s = Solution()

print(s.climbStairs2(1))
print(s.climbStairs2(2))
print(s.climbStairs2(3))
print(s.climbStairs2(4))
print(s.climbStairs2(5))
print(s.climbStairs2(6))
print(s.climbStairs2(0))
print(s.climbStairs2(44))