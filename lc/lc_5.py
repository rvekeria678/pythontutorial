# Leetcode Problem #5: Longest Palindrome Substring

# Description: Given a string s, return the longest palindrom substring in s

class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0
        l = ''

        while right < len(s):
            if s[left:]


s = Solution()

print(s.longestPalindrome('babad'))
print(s.longestPalindrome('cbbd'))
print(s.longestPalindrome('a'))