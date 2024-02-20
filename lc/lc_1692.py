# Leetcode Problem #1692: Richest Customer Wealth

# Description: You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        curr, max = 0,0
        for i in accounts:
            for j in i:
                curr += j
            max = curr if curr > max else max
            curr = 0
        return max

s = Solution()

l1 = [[1,2,3],[3,2,1]]
l2 = [[1,5],[7,3],[3,5]]

print(s.maximumWealth(l1))
print(s.maximumWealth(l2))