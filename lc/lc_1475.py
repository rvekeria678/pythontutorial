# Leetcode Problem #1475: Final Prices With a Special Discount in a Shop

# Description: You are given an integer array prices where prices[i] is the price of the ith item in a shop. There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all. Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.

class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        res = []
        for i in range(len(prices)):
            discount = 0
            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            res.append(prices[i]-discount)
        return res
    
class Solution2:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack = []
        for i in range(len(prices)):
            while stack and (prices[stack[-1]] >= prices[i]):
                prices[stack.pop()] -= prices[i]
            stack.append(i)
        return prices

s = Solution()
s2 = Solution2()

prices = [8,4,6,2,3]
print(s2.finalPrices(prices))
prices = [1,2,3,4,5]
print(s2.finalPrices(prices))

prices = [10,1,1,6]
print(s2.finalPrices(prices))
