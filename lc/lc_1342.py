# Leetcode Problem #1342: Number of Steps to Reduce a Number to Zero

# Description: Given an integer num, return the number of steps to reduce it to zero.In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while num:
            num = num ^ 1 if num & 1 else num >> 1
            ans += 1
        return ans
    
s = Solution()

num = 14
print(s.numberOfSteps(num))

num = 8
print(s.numberOfSteps(num))
