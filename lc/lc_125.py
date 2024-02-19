# Leetcode Problem #125: Valid Palindrome

# Description: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characers include letters and numbers. Given a string s, return true if it is a palindrom, or false otherwise

class Solution:
    def isPalindrome(self, s:str) -> bool:
        s = ''.join(char for char in s if char.isalnum()).lower()
        return s == s[::-1]
    

s = Solution()

print(s.isPalindrome('A man, a plan, a canal: Panama'))