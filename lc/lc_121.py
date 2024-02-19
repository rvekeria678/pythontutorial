# Leetcode Problem #121: Best Time to Buy and Sell Stock

# Description: You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock

class Solution:
    def maxProfit(self, prices: list[int]) -> int:        
        left, right, profit, current = 0, 1, 0, 0
        if len(prices) < 2:
            return 0

        while right < len(prices):
            print("LEFT:",prices[left],'; RIGHT:',prices[right])
            if prices[left] >= prices[right]:
                left = right
            else:
                current = prices[right] - prices[left]
                profit = current if profit < current else profit
            right += 1

        return profit
    
s = Solution()

l1 = [7,1,5,3,6,4]
l2 = [7,6,4,3,1]
l3 = [1,2,4,2,5,7,2,4,9,0,9]


print(s.maxProfit(l1))
print(s.maxProfit(l2))
print(s.maxProfit(l3))
