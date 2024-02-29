# Leetcode Problem #1768: Merge Strings Alternately

# Description: You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string. Return the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        overhead = min(len(word1), len(word2))
        for i in range(overhead):
            res += word1[i] + word2[i]
        return res + word1[overhead:] + word2[overhead:]

s = Solution()

word1 = "abc"
word2 = "pqr"
print(s.mergeAlternately(word1, word2))
word1 = "ab"
word2 = "pqrs"
print(s.mergeAlternately(word1, word2))

word1 = "abcd"
word2 = "pq"
print(s.mergeAlternately(word1, word2))

