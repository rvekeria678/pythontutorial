# Leetcode Problem #392: Is Subsequence

# Description: Given two strings s and t, return true if s is a subsequence of t, or false otherwise. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        curr = 0
        s_size = len(s)
        for i in range(len(t)):
            if s_size and s[curr] == t[i]:
                curr += 1
                if curr >= s_size:
                    return True 
        return True if not s_size else False

s = Solution()

word = "abc"
t = "ahbgdc"
print(s.isSubsequence(word, t))

word = "axc"
t = "ahbgdc"
print(s.isSubsequence(word, t))
