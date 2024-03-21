# Leetcode Problem #205: Isomorphic Strings

# Description: Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in s can be replaced to get t. All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for i in range(len(s)):
            if s[i] in d1:
                if d1[s[i]] != t[i]:
                    return False
            else:
                d1[s[i]] = t[i]
            if t[i] in d2:
                if d2[t[i]] != s[i]:
                    return False
            else:
                d2[t[i]] = s[i]
        return True

s = Solution()

t1 = "egg"
t2 = "add"
print(s.isIsomorphic(t1, t2))

t1 = "foo"
t2 = "bar"
print(s.isIsomorphic(t1, t2))

t1 = "paper"
t2 = "title"
print(s.isIsomorphic(t1, t2))

t1 = 'badc'
t2 = 'baba'
print(s.isIsomorphic(t1, t2))
