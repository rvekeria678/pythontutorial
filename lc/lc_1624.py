# Leetcode Problem #1624: Largest Substring Between Two Equal Characters

# Description: Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1. A substring is a contiguous sequence of characters within a string.

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = {}
        largest = -1
        for i in range(len(s)):
            if s[i] in seen:
                largest = max(largest, i - seen[s[i]] - 1)
            else:
                seen[s[i]] = i
        return largest

s = Solution()

stg = "aa"
print(s.maxLengthBetweenEqualCharacters(stg))

stg = "abca"
print(s.maxLengthBetweenEqualCharacters(stg))

stg = "cbzxy"
print(s.maxLengthBetweenEqualCharacters(stg))
