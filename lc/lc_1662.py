# Leetcode Problem 1662: Check if Two String Arrays are Equivalent

# Description: Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise. A string is represented by an array if the array elements concatenated in order forms the string.

class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        w1, w2 = "",""
        for i in word1:
            w1 += i
        for j in word2:
            w2 += j
        return w1 == w2

class Solution2:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return "".join(word1) == "".join(word2)

s = Solution()
s2 = Solution2()

word1 = ["ab","c"]
word2 = ["a", "bc"]

word3 = ["a", "cb"]
word4 = ["ab", "c"]

word5  = ["abc", "d", "defg"]
word6 = ["abcddefg"]

print(s.arrayStringsAreEqual(word1, word2))
print(s.arrayStringsAreEqual(word3,word4))
print(s.arrayStringsAreEqual(word5,word6))
