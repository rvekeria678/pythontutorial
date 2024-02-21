# Leetcode Problem #2859: Sum of Values at Indicies With K Set Bits

# Description: You are given a 0-indexed integer array nums and an integer k. Return an integer that denotes the sum of elements in nums whose corresponding indices have exactly k set bits in their binary representation. The set bits in an integer are the 1's present when it is written in binary.

class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        sum = 0
        for i,j in enumerate(nums):
            count = 0
            while i:
                if i & 1:
                    count += 1
                i >>= 1
            if count == k:
                sum += j
        return sum
s = Solution()

l1 = [5,10,1,5,2]
l2 = [4,3,2,1]

print(s.sumIndicesWithKSetBits(l1,1))
print(s.sumIndicesWithKSetBits(l2,2))
