# Leetcode Problem #2828: Check if a String Is an Acronym of Words

# Description: Given an array of strings words and a string s, determine if s is an acronym of words. The string s is considered an acronym of words if it can be formed by concatenating the first character of each string in words in order. For example, "ab" can be formed from ["apple", "banana"], but it can't be formed from ["bear", "aardvark"]. Return true if s is an acronym of words, and false otherwise.

class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        if len(words) != len(s):
            return False
        for i in range(len(words)):
            if words[i][0] != s[i]:
                return False
        return True

s = Solution()

words1 = ["alice","bob","charlie"]
s1 = "abc"

words2 = ["an","apple"]
s2 = "a"

words3 = ["never","gonna","give","up","on","you"]
s3 = "ngguoy"

print(s.isAcronym(words1, s1))
print(s.isAcronym(words2, s2))
print(s.isAcronym(words3, s3))