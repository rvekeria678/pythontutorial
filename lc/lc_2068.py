# Leetcode Problem #2068: Check Whether Two Strings are Almost Equivalent

# Description: Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3. Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost equivalent, or false otherwise. The frequency of a letter x is the number of times it occurs in the string.

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        freq = {}
        for character in word1:
            if character in freq:
                freq[character] += 1
            else:
                freq[character] = 1
        for character in word2:
            if character in freq:
                freq[character] -= 1
            else:
                freq[character] = -1
        for character in freq:
            if abs(freq[character]) > 3:
                return False
        return True

s = Solution()

word1 = "aaaa"
word2 = "bccb"
print(s.checkAlmostEquivalent(word1, word2))

word1 = "abcdeef"
word2 = "abaaacc"
print(s.checkAlmostEquivalent(word1, word2))

word1 = "cccddabba"
word2 = "babababab"
print(s.checkAlmostEquivalent(word1, word2))
