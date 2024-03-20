# Leetcode Problem #387: First Unique Character in a String

# Description: Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for character in s:
            if character in seen:
                seen[character] += 1
            else:
                seen[character] = 1
        for i in range(len(s)):
            if seen[s[i]] == 1:
                return i
        return -1

s = Solution()

st = "leetcode"
print(s.firstUniqChar(st))

st = "loveleetcode"
print(s.firstUniqChar(st))

st = "aabb"
print(s.firstUniqChar(st))
