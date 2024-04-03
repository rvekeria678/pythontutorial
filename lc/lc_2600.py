# Leetcode Problem #2600: K Items With the Maximum Sum

# Description: There is a bag that consists of items, each item has a number 1, 0, or -1 written on it. You are given four non-negative integers numOnes, numZeros, numNegOnes, and k. The bag initially contains: numOnes items with 1s written on them. numZeroes items with 0s written on them. numNegOnes items with -1s written on them. We want to pick exactly k items among the available items. Return the maximum possible sum of numbers written on the items.

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        maxsum = 0
        if numOnes and k > 0:
            maxsum += min(k, numOnes)
            k -= numOnes
        if numZeros and k > 0:
            k -= numZeros
        if numNegOnes and k > 0:
            maxsum -= k
        return maxsum

s = Solution()        

numOnes = 3
numZeros = 2
numNegOnes = 0
k = 2
print(s.kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k))

numOnes = 3
numZeros = 2
numNegOnes = 0
k = 4
print(s.kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k))






