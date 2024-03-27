# Leetcode Problem #5: Longest Palindrome Substring

# Description: Given a string s, return the longest palindrom substring in s

class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = ''
        for left in range(len(s)):
            for right in range(left, len(s)+1):
                if s[left:right] == s[left:right][::-1]:
                    m = s[left:right] if len(s[left:right]) > len(m) else m
        return m
    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, len(s)
        while left < right:
            


s = Solution()

print(s.longestPalindrome('babad'))
print(s.longestPalindrome('cbbd'))
print(s.longestPalindrome('a'))
print(s.longestPalindrome('bb'))