# Leetcode Problem: Minimum Number Game

# Description: You are given a 0-indexed integer array nums of even length and there is also an empty array arr. Alice and Bob decided to play a game where in every round Alice and Bob will do one move. The rules of the game are as follows:

# Every round, first Alice will remove the minimum element from nums, and then Bob does the same.

# Now, first Bob will append the removed element in the array arr, and then Alice does the same.

# The game continues until nums becomes empty.

# Return the resulting array arr.

class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        sorted_array = sorted(nums, reverse=True)
        result = []
        while len(sorted_array):
            alice = sorted_array.pop()
            bob = sorted_array.pop()
            result.append(bob)
            result.append(alice)
        return result

s = Solution()

l1 = [5,4,3,2]
l2 = [2,5]

print(s.numberGame(l1))
print(s.numberGame(l2))