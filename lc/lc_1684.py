# Leetcode Problem #1684: Count the Number of Consistent Strings

# Description: You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed. Return the number of consistent strings in the array words.

class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        count, consistent = 0, True 
        for word in words:
            for char in word:
                if char not in allowed:
                    consistent = False
            count = count + 1 if consistent else count
            consistent = True
        return count

s = Solution()

allowed1 = "ab"
words1 = ["ad","bd","aaab","baa","badab"]

allowed2 = "abc"
words2 = ["a","b","c","ab","ac","bc","abc"]

allowed3 = "cad" 
words3 = ["cc","acd","b","ba","bac","bad","ac","d"]

print(s.countConsistentStrings(allowed1, words1))
print(s.countConsistentStrings(allowed2, words2))
print(s.countConsistentStrings(allowed3, words3))