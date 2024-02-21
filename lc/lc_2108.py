# Leetcode Problem #2018: Find First Palindrome String in the Array

# Description: Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

# A string is palindromic if it reads the same forward and backward.

class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for i in words:
            if i == i[::-1]:
                return i
        return ""

s = Solution()

words1 = ["abc","car","ada","racecar","cool"]
words2 = ["notapalindrome","racecar"]
words3 = ["def","ghi"]

print(s.firstPalindrome(words1))
print(s.firstPalindrome(words2))
print(s.firstPalindrome(words3))

