# Leetcode Problem #70: Climbing Stairs

# Description: You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        steps = 1
        for i in range(n):
            steps = steps

        return steps


s = Solution()

print(s.climbStairs(2))
print(s.climbStairs(3))



