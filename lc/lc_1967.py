# Leetcode Problem #1967: Number of Strings that Appear as Substrings in Word

# Description: Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word. A substring is a contiguous sequence of characters within a string.

class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        count = 0
        for p in patterns:
            if p in word:
                count += 1
        return count

s = Solution()

patterns = ["a","abc","bc","d"]
word = "abc"
print(s.numOfStrings(patterns, word))

patterns = ["a","b","c"]
word = "aaaaabbbbb"
print(s.numOfStrings(patterns, word))

patterns = ["a","a","a"]
word = "ab"
print(s.numOfStrings(patterns, word))
