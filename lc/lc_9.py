# Leetcode Problem #9: Palindrome Number

# Description: Given an integer 'x', return true if 'x' is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
    
    def isPalindrome2(self, x:int) -> bool: # Much Faster
        x = str(x)
        return x == x[::-1]

    
s = Solution()

print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))