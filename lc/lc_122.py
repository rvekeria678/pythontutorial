# Leetcode Problem #122: Best Time to Buy and Sell Stock II

# Description: You are given an integer array prices where prices[i] is the price of a given stock on the ith day. On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day. Find and return the maximum profit you can achieve.

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left, right, size = 0, 1, len(prices)
        total = 0
        while left < size -1:
            if prices[left] < prices[right]:
                total += prices[right] - prices[left]
            left += 1
            right += 1

        return total

s = Solution()

prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))

prices = [1,2,3,4,5]
print(s.maxProfit(prices))

prices = [7,6,4,3,1]
print(s.maxProfit(prices))