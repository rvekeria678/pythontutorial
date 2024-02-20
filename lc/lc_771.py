# Leetcode Problem #771: Jewels and Stones

# Description: You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        record = {}
        count = 0
        for j in jewels:
            record[j] = 1
        for s in stones:
            if s in record:
                count += 1
        return count
    
s = Solution()

j1 = "aA"
j2 = "z"

s1 = "aAAbbbb"
s2 = "ZZ"

print(s.numJewelsInStones(j1,s1))
print(s.numJewelsInStones(j2,s2))
