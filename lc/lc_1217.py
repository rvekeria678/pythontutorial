# Leetcode Problem #1217: Minimum Cost to Move Chips to The Same Position:

# Description: We have n chips, where the position of the ith chip is position[i]. We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to: position[i] + 2 or position[i] - 2 with cost = 0; position[i] + 1 or position[i] - 1 with cost = 1. Return the minimum cost needed to move all the chips to the same position.

class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        evens = odds = 0
        for p in position:
            if p % 2: odds += 1
            else: evens += 1
        return evens if evens < odds else odds

s = Solution()

position = [1,2,3]
print(s.minCostToMoveChips(position))

position = [2,2,2,3,3]
print(s.minCostToMoveChips(position))

