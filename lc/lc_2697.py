# Leetcode Problem #2697: Lexicographically Smallest Palindrome

# Description: You are given a string s consisting of lowercase English letters, and you are allowed to perform operations on it. In one operation, you can replace a character in s with another lowercase English letter. Your task is to make s a palindrome with the minimum number of operations possible. If there are multiple palindromes that can be made using the minimum number of operations, make the lexicographically smallest one. A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b. Return the resulting palindrome string.

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left, right, res = 0, len(s)-1, ""

        while left < right:
            if s[left] != s[right]:
                res += s[left] if ord(s[left]) - ord(s[right]) <= 0 else s[right]
            else:
                res += s[left] 
            left += 1
            right -= 1
        return res + res[::-1] if len(s)%2==0 else res + s[len(s)//2] + res[::-1]
        
s = Solution()

str1 = "egcfe"
str2 = "abcd"
str3 = "seven"

print(s.makeSmallestPalindrome(str1))
print(s.makeSmallestPalindrome(str2))
print(s.makeSmallestPalindrome(str3))